"""
Script utiliser pour tester différrents algorithmes de classification sur nos données.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
# import svm
from sklearn.svm import SVC
# import random_forest
from sklearn.ensemble import RandomForestClassifier

### Chargement des données
df = pd.read_csv("lyrics.csv")

### Split en train et test
X = df.drop(columns=["Genre"])
y = df["Genre"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")

print(X_train)

### Vectoriser les données
vectorizer = TfidfVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train["Parole"])
X_test_vectorized = vectorizer.transform(X_test["Parole"])

### Entraîner le modèle

model = RandomForestClassifier()
model.fit(X_train_vectorized, y_train)

### Prédictions
y_pred = model.predict(X_test_vectorized)
print(y_pred)

### Évaluation du modèle
print(classification_report(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=model.classes_, yticklabels=model.classes_)
plt.xlabel("Prédictions")
plt.ylabel("Vérités")
plt.title("Matrice de confusion")
plt.show()