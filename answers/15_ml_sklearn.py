"""
Answers for 15_ml_sklearn - try the questions first!
"""

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# ------------------------------------------------------------------
# ml_workflow.py
# ------------------------------------------------------------------
# (same mini-dataset as the lesson)
rng = np.random.default_rng(42)
n = 300
age = rng.integers(18, 70, n)
income_k = rng.normal(45, 15, n).round(1)
visits = rng.integers(0, 20, n)
tilt = (income_k - 45) / 15 + (visits - 10) / 5 - (age - 35) / 20
subscribed = (tilt + rng.normal(0, 1.2, n) > 0.2).astype(int)
df = pd.DataFrame({"age": age, "income_k": income_k,
                   "visits": visits, "subscribed": subscribed})
X, y = df[["age", "income_k", "visits"]], df["subscribed"]
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)

# Q1: The model has already SEEN the training answers, so a train
#     score only proves memorization; the honest number comes from
#     rows held out of fitting (or from cross-validation).
model = LogisticRegression(max_iter=1000).fit(X_tr, y_tr)
print("wf Q1: train", round(model.score(X_tr, y_tr), 3),
      "vs test", round(model.score(X_te, y_te), 3))

# Q2: train_test_split shuffles randomly on every call, so each run
#     trains/tests on different rows and scores wobble. Passing
#     random_state pins the shuffle: identical split every run.
a = train_test_split(X, y, test_size=0.25)[0]
b = train_test_split(X, y, test_size=0.25)[0]
print("wf Q2: same rows without random_state?", a.index.equals(b.index))
c = train_test_split(X, y, test_size=0.25, random_state=42)[0]
d = train_test_split(X, y, test_size=0.25, random_state=42)[0]
print("wf Q2: same rows with random_state?", c.index.equals(d.index))

# Q3: Swap the estimator, keep the split -- that is the whole
#     recipe. KNN votes on the 5 nearest training rows, so it is
#     more at the mercy of unscaled features than logistic
#     regression, which fits one smooth equation.
knn = KNeighborsClassifier(n_neighbors=5).fit(X_tr, y_tr)
print("wf Q3: knn", round(knn.score(X_te, y_te), 3),
      "vs logistic", round(model.score(X_te, y_te), 3))

# Q4: coef_ holds one weight per feature: sign = push direction,
#     size = strength. Here visits (+0.24) raises the odds the most
#     -- people who keep returning to the pricing page really buy.
print("wf Q4: coefs", model.coef_.round(2)[0],
      "intercept", model.intercept_.round(2)[0])

# ------------------------------------------------------------------
# model_evaluation.py
# ------------------------------------------------------------------
# (same imbalanced fraud dataset as the lesson)
rng = np.random.default_rng(7)
n_okay, n_big, n_small = 950, 35, 15
tx = pd.DataFrame({
    "amount": np.concatenate([rng.normal(60, 25, n_okay).clip(5),
                              rng.normal(450, 80, n_big),
                              rng.normal(55, 18, n_small)]).round(2),
    "hour": rng.integers(0, 24, n_okay + n_big + n_small),
    "fraud": np.concatenate([np.zeros(n_okay, int),
                             np.ones(n_big + n_small, int)]),
})
X, y = tx[["amount", "hour"]], tx["fraud"]
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)

# Q1: ZERO frauds caught: its 0.952 accuracy is just the 95% okay
#     rows it always predicts. On the fraud class, precision and
#     recall are both 0 -- accuracy alone hides a useless model.
dummy = DummyClassifier(strategy="most_frequent").fit(X_tr, y_tr)
print("ev Q1: dummy acc", round(dummy.score(X_te, y_te), 3),
      "frauds caught", int((dummy.predict(X_te) == 1).sum()))

# Q2: Screening pushes RECALL -- a missed cancer (fn) can be fatal
#     while a false alarm (fp) only costs one more test. Spam
#     filtering pushes PRECISION -- losing a real email (fp) hurts
#     far more than one spam in the inbox (fn).
model = LogisticRegression(max_iter=1000).fit(X_tr, y_tr)
y_pred = model.predict(X_te)
tn, fp, fn, tp = (int(v) for v in confusion_matrix(y_te, y_pred).ravel())
print("ev Q2: precision", round(tp / (tp + fp), 3),
      "recall", round(tp / (tp + fn), 3))

# Q3: The arguments are swapped -- it is confusion_matrix(y_true,
#     y_pred). Reversed, every box flips (tn<->tp, fn<->fp), so the
#     "recall" it reports belongs to an upside-down world: 8 caught
#     frauds turn into 0.
bad = confusion_matrix(y_pred, y_te).ravel().tolist()
print("ev Q3: swapped", tuple(bad), "vs correct", (tn, fp, fn, tp))

# Q4: The dummy's cv mean is the bar to clear: the real model beats
#     it on accuracy AND turns 0 caught frauds into most of them --
#     the metric that actually matters for this business.
cv_dummy = cross_val_score(DummyClassifier(strategy="most_frequent"),
                           X, y, cv=5)
cv_model = cross_val_score(model, X, y, cv=5)
print("ev Q4: dummy", round(cv_dummy.mean(), 3),
      "vs model", round(cv_model.mean(), 3))

# ------------------------------------------------------------------
# preprocessing.py
# ------------------------------------------------------------------
# (same messy bike-shop dataset as the lesson)
rng = np.random.default_rng(3)
n = 300
city = rng.choice(["Berlin", "Lisbon", "Krakow"], n, p=[0.5, 0.3, 0.2])
df = pd.DataFrame({"age": rng.integers(18, 70, n),
                   "income_eur": (rng.normal(42, 14, n) * 1000).round(0),
                   "city": city})
tilt = ((df["income_eur"] - 42000) / 14000 + (45 - df["age"]) / 25
        + (city == "Berlin") * 0.6)
df["bought"] = (tilt + rng.normal(0, 0.7, n) > 0.5).astype(int)
X, y = df[["age", "income_eur", "city"]], df["bought"]
X_tr, X_te, y_tr, y_te = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)
num_cols = ["age", "income_eur"]

# Q1: Fitting the scaler on ALL rows lets the test set's mean/std
#     seep into the training inputs, so the test score no longer
#     describes unseen data. Here the two happen to tie at 0.787 --
#     leakage does not always move the score, but it always
#     invalidates it. The fix: fit on train rows only, or wrap
#     everything in a Pipeline and never think about it again.
leaky = StandardScaler().fit(X[num_cols])       # saw test rows too
honest = StandardScaler().fit(X_tr[num_cols])   # train rows only
knn_leaky = KNeighborsClassifier(5).fit(leaky.transform(X_tr[num_cols]), y_tr)
knn_honest = KNeighborsClassifier(5).fit(honest.transform(X_tr[num_cols]), y_tr)
print("pp Q1: leaky", round(knn_leaky.score(leaky.transform(X_te[num_cols]), y_te), 3),
      "honest", round(knn_honest.score(honest.transform(X_te[num_cols]), y_te), 3))

# Q2: Without handle_unknown="ignore" the strict encoder raises
#     ValueError on the unseen city. With "ignore" the row simply
#     gets all-zero city columns: "no city info", and no crash.
ohe_strict = OneHotEncoder(sparse_output=False).fit(df[["city"]])
try:
    ohe_strict.transform(pd.DataFrame([{"city": "Oslo"}]))
except ValueError as err:
    print("pp Q2: strict ->", str(err).split("\n")[0][:55], "...")
ohe_safe = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
row = ohe_safe.fit(df[["city"]]).transform(pd.DataFrame([{"city": "Oslo"}]))
print("pp Q2: ignore ->", row[0].astype(int))

# Q3: A fresh scaler on test would shift test rows by TEST-set
#     numbers while the model learned from TRAIN-set numbers -- the
#     two worlds stop matching and every prediction skews. One
#     fitted scaler, two calls: fit on train, transform both.
s_tr = StandardScaler().fit(X_tr[num_cols])
s_te = StandardScaler().fit(X_te[num_cols])
print("pp Q3: train-fit means", s_tr.mean_.round(1).tolist(),
      "vs test-fit means", s_te.mean_.round(1).tolist())

# Q4: cross_val_score clones the WHOLE pipeline per fold, re-fitting
#     scaler and encoder on each fold's train part -- so even across
#     folds, no fold's prep ever sees another fold's rows.
prep = ColumnTransformer([
    ("num", StandardScaler(), num_cols),
    ("cat", OneHotEncoder(handle_unknown="ignore"), ["city"]),
])
pipe = Pipeline([("prep", prep),
                 ("model", LogisticRegression(max_iter=1000))])
cv = cross_val_score(pipe, X, y, cv=5)
print("pp Q4: pipeline cv", cv.round(3), "mean", round(cv.mean(), 3))
