"""
=====================================================================
TOPIC: Model Evaluation -- When Accuracy Lies
=====================================================================

SCENARIO
--------
A payments company flags fraudulent card transactions. Fraud is rare:
only 5 in every 100 rows. A "model" that always says NOT FRAUD is 95%
accurate -- and catches zero frauds. Before shipping anything we need
numbers that expose that trick and describe the alarms we really get.

TOPIC
-----
Accuracy = share of correct predictions -- it lies on imbalanced data.
The confusion matrix counts every outcome: tn, fp, fn, tp (.ravel()).
  tn / fp = okay rows called okay / called fraud (false alarms)
  fn / tp = frauds missed / frauds caught
precision = tp/(tp+fp): when we raise the alarm, how often are we right?
  Spam cares -- never bury a real email in the spam folder.
recall = tp/(tp+fn): of all the real cases, how many did we catch?
  Medicine cares -- never send a sick patient home untested.
classification_report prints both, per class. DummyClassifier is the
baseline you must beat, and cross_val_score(model, X, y, cv=5)
re-fits on 5 different splits -- far more honest than one split.

Run: python 15_ml_sklearn/model_evaluation.py
Answers: answers/15_ml_sklearn.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------
import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score, train_test_split

# A deliberately imbalanced dataset: 1000 transactions, 50 frauds.
# 35 are big purchases; 15 are small "probes" that look innocent.
rng = np.random.default_rng(7)
n_okay, n_big, n_small = 950, 35, 15
tx = pd.DataFrame({
    # big frauds spend wildly more -- that is the learnable pattern:
    "amount": np.concatenate([rng.normal(60, 25, n_okay).clip(5),
                              rng.normal(450, 80, n_big),
                              rng.normal(55, 18, n_small)]).round(2),
    "hour": rng.integers(0, 24, n_okay + n_big + n_small),
    "fraud": np.concatenate([np.zeros(n_okay, int),
                             np.ones(n_big + n_small, int)]),
})
X, y = tx[["amount", "hour"]], tx["fraud"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)

# The trick baseline: always predict the majority class.
dummy = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)
print("dummy accuracy:", round(dummy.score(X_test, y_test), 3))
print("dummy frauds caught:", int((dummy.predict(X_test) == 1).sum()))

# A real model: logistic regression learns the big-amount pattern.
# The small probes are indistinguishable, so recall never hits 1.0 --
# exactly the honest picture a confusion matrix is for.
model = LogisticRegression(max_iter=1000).fit(X_train, y_train)
y_pred = model.predict(X_test)
print("model accuracy:", round(model.score(X_test, y_test), 3))

# The confusion matrix tells the story accuracy hides:
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
print(f"matrix  tn={tn} fp={fp} fn={fn} tp={tp}")
print("precision:", round(tp / (tp + fp), 3),
      "recall:", round(tp / (tp + fn), 3))

print(classification_report(y_test, y_pred, digits=2))

# One call, five honest scores: cv=5 re-fits on 5 different splits,
# so one lucky split cannot flatter a bad model.
scores = cross_val_score(model, X, y, cv=5)
print("cv mean:", round(scores.mean(), 3), "+/-", round(scores.std(), 3))

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/15_ml_sklearn.py
# ------------------------------------------------------------------
# Q1: Predict the output -- the all-"not-fraud" dummy scores ~0.95
#     accuracy here. How many frauds does it catch, and why is that
#     a disaster even though the accuracy looks great?
#
# Q2: Concept check -- a cancer screening test and a spam filter both
#     trade precision against recall. Which one should push RECALL
#     up, and which one PRECISION? Justify each in one sentence.
#
# Q3: Spot the bug -- a teammate wrote this and their counts are all
#     in the wrong boxes (tn looks like tp). What is swapped?
#         tn, fp, fn, tp = confusion_matrix(y_pred, y_test).ravel()
#
# Q4: Write code: run cross_val_score(cv=5) with a
#     DummyClassifier(strategy="most_frequent") and print the mean.
#     Your real model must beat that number -- does it?
