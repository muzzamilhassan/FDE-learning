"""
Solution for Project 07 - First ML Classifier (sklearn).

Run it with:
    python answers/projects/project_07_ml_classifier_solution.py

Generates a synthetic PulseFit dataset from rules (500 members, 5
usage features, a renewal label with noise), then runs the full
workflow: split with a fixed seed, DummyClassifier baseline,
LogisticRegression with accuracy + classification report, 5-fold
cross-validation, predictions for three hand-made members, and the
stretch comparison of a scaled Pipeline vs a DecisionTree.
No downloads, no API keys.
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

FEATURES = ["monthly_logins", "avg_session_min", "support_tickets",
            "days_since_login", "is_pro"]


def make_dataset(n: int = 500) -> tuple[pd.DataFrame, pd.Series]:
    """A synthetic dataset with a real (noisy) pattern hidden in it."""
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


def split_data(X: pd.DataFrame, y: pd.Series):
    """Task 2: one honest split, frozen by random_state."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y)
    print(f"  train: {len(X_train)} members | test: {len(X_test)} members")
    print("  random_state=42 -> same split every run (results reproducible);")
    print("  stratify=y -> both halves keep the same renew/churn ratio.")
    return X_train, X_test, y_train, y_test


def baseline_accuracy(X_train, X_test, y_train, y_test) -> float:
    """Task 3: the do-nothing score every real model must beat."""
    dummy = DummyClassifier(strategy="most_frequent")
    dummy.fit(X_train, y_train)
    accuracy = accuracy_score(y_test, dummy.predict(X_test))
    print(f"  DummyClassifier accuracy: {accuracy:.3f}")
    print("  (it predicts the majority class every single time)")
    return accuracy


def train_logistic(X_train, X_test, y_train, y_test):
    """Task 4: the real model, with the honest evaluation."""
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print(f"  LogisticRegression accuracy: "
          f"{accuracy_score(y_test, predictions):.3f}")
    print("\n  classification report (0 = churn, 1 = renew):")
    print(classification_report(y_test, predictions, digits=3))
    print("  reading it: for class 0, recall = 'of the members who really")
    print("  churned, how many did we catch?' -- that is the number support")
    print("  cares about, because a missed churner is a lost subscription.")
    return model


def cross_validate(X: pd.DataFrame, y: pd.Series) -> None:
    """Task 5: five folds instead of one lucky split."""
    scores = cross_val_score(LogisticRegression(max_iter=1000), X, y, cv=5)
    print("  fold accuracies: " + ", ".join(f"{s:.3f}" for s in scores))
    print(f"  mean {scores.mean():.3f} +- {scores.std():.3f}")
    print("  (a small std means the score is stable, not split-luck.)")


def predict_members(model) -> None:
    """Task 6: three hand-made members through the fitted model."""
    members = pd.DataFrame([
        # super-user: heavy usage, no problems, just active
        {"monthly_logins": 55, "avg_session_min": 80,
         "support_tickets": 0, "days_since_login": 1, "is_pro": 1},
        # ghost: barely uses the app, gone for weeks
        {"monthly_logins": 2, "avg_session_min": 5,
         "support_tickets": 1, "days_since_login": 40, "is_pro": 0},
        # ticket magnet: decent usage but drowning in support tickets
        {"monthly_logins": 20, "avg_session_min": 30,
         "support_tickets": 7, "days_since_login": 4, "is_pro": 1},
    ])
    probabilities = model.predict_proba(members)[:, 1]
    print("  (columns match FEATURES, order matters)")
    for (_, member), probability in zip(members.iterrows(), probabilities):
        verdict = "will renew" if probability >= 0.5 else "will CHURN"
        print(f"  logins={member.monthly_logins:>2} min={member.avg_session_min:>2}"
              f" tickets={member.support_tickets} idle={member.days_since_login:>2}d"
              f" pro={member.is_pro} -> P(renew)={probability:.2f} ({verdict})")


def stretch_compare(X: pd.DataFrame, y: pd.Series) -> None:
    """Task 7: scaler+logreg pipeline vs decision tree."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y)
    models = [
        ("pipeline(StandardScaler+LogReg)",
         Pipeline([("scale", StandardScaler()),
                   ("model", LogisticRegression(max_iter=1000))])),
        ("DecisionTreeClassifier",
         DecisionTreeClassifier(random_state=42)),
    ]
    for name, model in models:
        model.fit(X_train, y_train)
        accuracy = accuracy_score(y_test, model.predict(X_test))
        print(f"  {name:<36} test accuracy: {accuracy:.3f}")
    print("  takeaway: scaling changed little here (the features already")
    print("  share a rough range), but the pipeline is the habit to keep --")
    print("  logreg NEEDS scaled features to be fair; the tree does not care.")
    print("  A single unconstrained tree memorizes noise, so logreg ships.")


def main() -> None:
    print("FIRST ML CLASSIFIER -- solution")

    print("\nStep 1: the data")
    X, y = make_dataset()
    print(f"  {len(X)} members, {len(FEATURES)} features: {FEATURES}")
    balance = y.value_counts(normalize=True).round(3)
    print(f"  class balance: {balance.to_dict()}  (1 = will renew)")
    print(f"  so a model that always says 'renew' scores ~{balance.get(1, 0):.2f}.")

    print("\nStep 2: split")
    X_train, X_test, y_train, y_test = split_data(X, y)

    print("\nStep 3: baseline")
    baseline_accuracy(X_train, X_test, y_train, y_test)

    print("\nStep 4: logistic regression")
    model = train_logistic(X_train, X_test, y_train, y_test)

    print("\nStep 5: cross-validation")
    cross_validate(X, y)

    print("\nStep 6: three hand-made members")
    predict_members(model)

    print("\nStep 7 (stretch): pipeline vs tree")
    stretch_compare(X, y)

    print("\nTrained, evaluated, and honest about it. That is the whole job.")


if __name__ == "__main__":
    main()
