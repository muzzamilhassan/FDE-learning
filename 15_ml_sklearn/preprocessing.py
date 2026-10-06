"""
=====================================================================
TOPIC: Preprocessing & Pipelines -- Feeding Models Clean Numbers
=====================================================================

SCENARIO
--------
A bike-shop chain wants to predict which customers will buy an
e-bike. The raw table is messy: age in years, income in EUROS
(huge numbers), city as text. Models are just math -- they need
numbers on similar scales and text turned into columns, applied the
SAME way at prediction time as at training time.

TOPIC
-----
StandardScaler rescales each numeric column to mean 0, std 1 --
distance models like KNN compare features, so a column with big
values (income) otherwise drowns out the rest (age).
OneHotEncoder turns one text column into one 0/1 column per category.
ColumnTransformer applies different prep to different columns.
Pipeline chains prep + model into one object: .fit(X, y) and
.predict(raw_rows) just work, even for one brand-new row.
THE golden rule: fit prep on TRAIN rows only. Fitting on all the
data leaks test-set info into training and inflates scores -- a
Pipeline makes that leak impossible by construction.

Run: python 15_ml_sklearn/preprocessing.py
Answers: answers/15_ml_sklearn.py
=====================================================================
"""

# ------------------------------------------------------------------
# TOPIC EXAMPLES
# ------------------------------------------------------------------
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# A mixed messy table: numbers of wildly different sizes + text.
rng = np.random.default_rng(3)
n = 300
city = rng.choice(["Berlin", "Lisbon", "Krakow"], n, p=[0.5, 0.3, 0.2])
df = pd.DataFrame({"age": rng.integers(18, 70, n),
                   "income_eur": (rng.normal(42, 14, n) * 1000).round(0),
                   "city": city})
# Buyers: higher income, younger, and Berliners love e-bikes.
tilt = ((df["income_eur"] - 42000) / 14000 + (45 - df["age"]) / 25
        + (city == "Berlin") * 0.6)
df["bought"] = (tilt + rng.normal(0, 0.7, n) > 0.5).astype(int)

X, y = df[["age", "income_eur", "city"]], df["bought"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y)

# -- Why scaling matters: KNN compares DISTANCES between rows ------
raw = KNeighborsClassifier(5).fit(X_train[["age", "income_eur"]], y_train)
print("KNN raw    :", round(raw.score(X_test[["age", "income_eur"]], y_test), 3))

scaler = StandardScaler().fit(X_train[["age", "income_eur"]])  # TRAIN rows only
Xtr_s = scaler.transform(X_train[["age", "income_eur"]])
Xte_s = scaler.transform(X_test[["age", "income_eur"]])  # reuse TRAIN stats
scaled = KNeighborsClassifier(5).fit(Xtr_s, y_train)
print("KNN scaled :", round(scaled.score(Xte_s, y_test), 3))

# Text can't be averaged or subtracted -- encode it into 0/1 columns.
ohe = OneHotEncoder(sparse_output=False,
                    handle_unknown="ignore").fit(df[["city"]])
print("city ->", list(ohe.get_feature_names_out()))

# -- ColumnTransformer + Pipeline: the professional one-liner ------
prep = ColumnTransformer([
    ("num", StandardScaler(), ["age", "income_eur"]),
    ("cat", OneHotEncoder(handle_unknown="ignore"), ["city"]),
])
pipe = Pipeline([("prep", prep), ("model", LogisticRegression(max_iter=1000))])
pipe.fit(X_train, y_train)   # scaler/encoder fit on TRAIN rows ONLY
print("pipeline test accuracy:", round(pipe.score(X_test, y_test), 3))

# One raw row in -- the SAME fitted prep runs, then the model:
new_row = pd.DataFrame([{"age": 41, "income_eur": 52000, "city": "Oslo"}])
print("new customer (unseen city):", pipe.predict(new_row),
      "P(buy):", pipe.predict_proba(new_row)[0, 1].round(2))

# ------------------------------------------------------------------
# QUESTIONS - try them yourself, then check answers/15_ml_sklearn.py
# ------------------------------------------------------------------
# Q1: Spot the bug -- this scores slightly higher on test, but the
#     number is a lie. Which line leaks, and why is it wrong?
#         X_tr, X_te, y_tr, y_te = train_test_split(X, y)
#         scaler = StandardScaler().fit(X)     # <-- culprit
#         knn.fit(scaler.transform(X_tr), y_tr)
#         print(knn.score(scaler.transform(X_te), y_te))
#
# Q2: Predict the output/error -- you fit the OneHotEncoder WITHOUT
#     handle_unknown="ignore", then predict on a row whose city is
#     "Oslo", never seen in training. What happens? Which argument
#     fixes it, and what does that row's city columns become?
#
# Q3: Concept check -- why must the SAME fitted scaler (not a fresh
#     StandardScaler) transform the test rows?
#
# Q4: Write code: wrap the ColumnTransformer + LogisticRegression
#     Pipeline in cross_val_score(pipe, X, y, cv=5) and print the
#     mean -- cross-validation re-runs the whole pipeline per split,
#     so no fold's prep ever sees another fold's rows.
