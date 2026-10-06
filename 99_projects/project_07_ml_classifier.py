"""
=====================================================================
PROJECT: First ML Classifier  (Difficulty: intermediate)
=====================================================================

SCENARIO
--------
You are on the growth team of "PulseFit", a fitness app with a
monthly subscription. Support keeps asking: "which members are about
to churn?" Your job is to train the company's FIRST machine-learning
model -- a classifier that predicts will_renew from a member's usage
numbers -- and to compare it honestly against a do-nothing baseline
before anyone gets carried away.

WHAT YOU WILL PRACTICE
----------------------
- Features X and labels y (from module 15)
- train_test_split with a fixed random_state and stratify (module 15)
- DummyClassifier: the "do nothing" baseline every model must beat (module 15)
- LogisticRegression: fit, predict, accuracy_score (module 15)
- classification_report: precision / recall / f1 (module 15)
- cross_val_score: accuracy across 5 folds (module 15)
- Pipeline + StandardScaler and DecisionTree (module 15, stretch)

YOUR TASKS
----------
1. Run make_dataset() (done for you) and print the class balance with
   y.value_counts(normalize=True). What would a useless model score?
2. split_data(): train_test_split(..., test_size=0.25, random_state=42,
   stratify=y). Why fix random_state? Why stratify?
3. baseline_accuracy(): fit DummyClassifier(strategy="most_frequent")
   on the train set, score it on the test set. This is the score to beat.
4. train_logistic(): fit LogisticRegression(max_iter=1000), then print
   accuracy_score AND classification_report on the test set. Which
   mistake hurts more here: a false "will renew" or a false "will churn"?
5. cross_validate(): cross_val_score(..., cv=5) -- report mean and std.
   Is the score stable across folds?
6. predict_members(model): predict renewal for 3 hand-made members
   (a super-user, a ghost, a ticket magnet) with predict_proba too.
7. Stretch: stretch_compare(): a Pipeline(StandardScaler(),
   LogisticRegression()) vs DecisionTreeClassifier -- compare test
   accuracy and decide which one you would ship.

STARTER CODE
------------
Complete the TODOs below. Run with:
    python 99_projects/project_07_ml_classifier.py

No downloads, no API keys: the dataset is generated from rules.
Hints are inline. A full solution is in answers/projects/.
=====================================================================
"""

from __future__ import annotations

import random

import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
# (every import above becomes useful as you complete the TODOs)

FEATURES = ["monthly_logins", "avg_session_min", "support_tickets",
            "days_since_login", "is_pro"]


def make_dataset(n: int = 500) -> tuple[pd.DataFrame, pd.Series]:
    """Done for you: a synthetic dataset with a REAL pattern hidden in it.

    Every row is one member. Renewal likelihood rises with logins,
    session length and the pro-plan bump, and falls with open support
    tickets and days since the last login -- plus noise, like life.
    """
    rng = random.Random(7)
    rows, labels = [], []
    for _ in range(n):
        is_pro = 1 if rng.random() < 0.4 else 0
        logins = rng.randint(0, 60)
        minutes = rng.randint(1, 90)
        tickets = rng.randint(0, 8)
        idle = rng.randint(0, 45)
        score = (0.05 * logins + 0.015 * minutes - 0.20 * tickets
                 - 0.06 * idle + 0.40 * is_pro + rng.uniform(-0.7, 0.7))
        rows.append({
            "monthly_logins": logins,
            "avg_session_min": minutes,
            "support_tickets": tickets,
            "days_since_login": idle,
            "is_pro": is_pro,
        })
        labels.append(1 if score > 0 else 0)
    return pd.DataFrame(rows, columns=FEATURES), pd.Series(labels, name="will_renew")


# ------------------------------------------------------------------
# TODOs -- everything below is yours
# ------------------------------------------------------------------

def split_data(X: pd.DataFrame, y: pd.Series):
    """TODO 2: return train_test_split(X, y, test_size=0.25,
    random_state=42, stratify=y) -- that is 4 return values.

    Print the train/test sizes so the split is visible.
    """
    print("TODO: implement split_data()")
    return None, None, None, None


def baseline_accuracy(X_train, X_test, y_train, y_test) -> float | None:
    """TODO 3: DummyClassifier(strategy="most_frequent").

    fit it on the TRAIN set only, predict on X_test, score with
    accuracy_score(y_test, ...). Print and return the accuracy.
    """
    print("TODO: implement baseline_accuracy()")
    return None


def train_logistic(X_train, X_test, y_train, y_test):
    """TODO 4: LogisticRegression(max_iter=1000).

    fit on the train set, predict on X_test, then print BOTH
    accuracy_score and classification_report(y_test, predictions).
    Return the fitted model (needed by task 6).
    """
    print("TODO: implement train_logistic()")
    return None


def cross_validate(X: pd.DataFrame, y: pd.Series) -> None:
    """TODO 5: scores = cross_val_score(LogisticRegression(max_iter=1000),
    X, y, cv=5). Print each fold score, then mean and std."""
    print("TODO: implement cross_validate()")


def predict_members(model) -> None:
    """TODO 6: build a 3-row DataFrame with the SAME columns as FEATURES:

    - a super-user: high logins, long sessions, no tickets, logged in today
    - a ghost: barely any logins, tiny sessions, weeks since last login
    - a ticket magnet: medium usage but 7 open support tickets
    Then print model.predict(members) AND model.predict_proba(members).
    (predict_proba column 1 is P(renew).)
    """
    print("TODO: implement predict_members()")


def stretch_compare(X: pd.DataFrame, y: pd.Series) -> None:
    """TODO 7 (stretch): make a fresh split, then fit two models and
    compare test accuracy:

    - Pipeline([("scale", StandardScaler()), ("model", LogisticRegression(max_iter=1000))])
    - DecisionTreeClassifier(random_state=42)

    Which would you ship? One or two printed sentences of reasoning count.
    """
    print("TODO: implement stretch_compare()")


def main() -> None:
    print("=" * 58)
    print("  FIRST ML CLASSIFIER -- starter")
    print("  Train, evaluate, and compare honestly.")
    print("=" * 58)

    print("\nStep 1: the data")
    X, y = make_dataset()
    print(f"  {len(X)} members, {len(FEATURES)} features: {FEATURES}")
    print(f"  class balance: {y.value_counts(normalize=True).round(3).to_dict()}")
    print("  (a model that always says 'renew' scores this -- beat it)")

    print("\nStep 2: split")
    X_train, X_test, y_train, y_test = split_data(X, y)
    if X_train is None:
        print("  implement split_data() to continue.")
        return

    print("\nStep 3: baseline")
    if baseline_accuracy(X_train, X_test, y_train, y_test) is None:
        print("  implement baseline_accuracy() to continue.")
        return

    print("\nStep 4: logistic regression")
    model = train_logistic(X_train, X_test, y_train, y_test)
    if model is None:
        print("  implement train_logistic() to continue.")
        return

    print("\nStep 5: cross-validation")
    cross_validate(X, y)

    print("\nStep 6: three hand-made members")
    predict_members(model)

    print("\nStep 7 (stretch): pipeline vs tree")
    stretch_compare(X, y)

    print("\nDone -- did your model beat the dummy? By how much?")


if __name__ == "__main__":
    main()
