"""
=====================================================================
TOPIC: The ML Workflow -- Your First Model
=====================================================================

SCENARIO
--------
A streaming service calls customers to pitch a premium plan. Calls
cost money, so the team wants to predict WHO will subscribe before
dialing. We have 300 past customers: their age, income and how many
times they visited the pricing page, plus whether they subscribed.

TOPIC
-----
Plain-words terms:
- feature (X): the input columns a model learns from (age, income...)
- target (y): the answer to predict -- here "subscribed": 0 or 1
- classification predicts a category; regression predicts a number
The universal recipe: split -> pick a model -> .fit() -> .score().
random_state pins the shuffle so every run gets the SAME split;
omit it and scores wobble run to run (or a bug hides behind luck).
Never grade a model on its training rows: it has already seen those
answers, so a perfect train score just proves memorization.

Run: python 15_ml_sklearn/ml_workflow.py
Answers: answers/15_ml_sklearn.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# -- 1. A tiny in-memory dataset -----------------------------------
rng = np.random.default_rng(42)
n = 300
age = rng.integers(18, 70, n)              # feature: years
income_k = rng.normal(45, 15, n).round(1)  # feature: income, thousands
visits = rng.integers(0, 20, n)            # feature: pricing-page visits
# Subscribing follows a pattern plus some real-world noise:
tilt = (income_k - 45) / 15 + (visits - 10) / 5 - (age - 35) / 20
subscribed = (tilt + rng.normal(0, 1.2, n) > 0.2).astype(int)

df = pd.DataFrame({"age": age, "income_k": income_k,
                   "visits": visits, "subscribed": subscribed})
print(df["subscribed"].value_counts().to_dict(), "<- class balance")

# -- 2. Split FIRST: hold out rows the model never trains on -------
X = df[["age", "income_k", "visits"]]      # features: a 2-D table
y = df["subscribed"]                       # target: a 1-D column
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)

# -- 3. Pick a model and teach it the training rows ----------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)                # ALL of the learning happens here

# -- 4. Grade it on rows it has NEVER seen -------------------------
print("train accuracy:", round(model.score(X_train, y_train), 3))
print("test  accuracy:", round(model.score(X_test, y_test), 3))

# -- 5. Use it on brand-new customers ------------------------------
new_customers = pd.DataFrame({"age": [24, 58],
                              "income_k": [78.0, 22.0],
                              "visits": [16, 1]})
print("predicted:", model.predict(new_customers))
print("P(subscribe):", model.predict_proba(new_customers)[:, 1].round(2))

# The model is just an equation -- you can read its coefficients:
print("coefs (age, income_k, visits):", model.coef_.round(2)[0])

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/15_ml_sklearn.py
# ------------------------------------------------------------------
# Q1: Predict the output -- a teammate runs model.score(X_train,
#     y_train), sees ~0.81 and says "ship it". What is wrong with
#     grading a model on the very rows it trained on?
#
# Q2: Spot the bug -- this script prints a slightly different score
#     every time it runs. One argument fixes it. Which one, and why?
#         X_tr, X_te, y_tr, y_te = train_test_split(X, y,
#                                                   test_size=0.25)
#         model = LogisticRegression(max_iter=1000).fit(X_tr, y_tr)
#         print(model.score(X_te, y_te))
#
# Q3: Write code: train a KNeighborsClassifier(n_neighbors=5) on the
#     SAME split and print its test accuracy next to the logistic
#     regression's. (from sklearn.neighbors import KNeighborsClassifier)
#
# Q4: Write code: print model.coef_ and name the feature that raises
#     the odds of subscribing the most. Does its sign make sense?
