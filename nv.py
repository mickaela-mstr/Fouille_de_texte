"""
Script utiliser pour tester différrents algorithmes de classification sur nos données.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, confusion_matrix


def load_data(csv_path="lyrics.csv"):
    """chargement des données"""
    
    df = pd.read_csv(csv_path)
    return df

def split_data(df):
    """split les données en jeu d'entraînement et de test"""
    X = df.drop(columns=["Genre"])
    y = df["Genre"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    print(f"X_train shape: {X_train.shape}")
    print(f"X_test shape: {X_test.shape}")
    print(X_train)

    return train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

def vectorize_text(X_train, X_test, text_column="Parole"):
    """Vectorise les textes avec TF-IDF"""
    vectorizer = TfidfVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train[text_column])
    X_test_vec = vectorizer.transform(X_test[text_column])

    return X_train_vec, X_test_vec, vectorizer


def evaluate_model(name, model, X_test_vec, y_test):
    """Affiche le rapport de classification et la matrice de confusion"""
    y_pred = model.predict(X_test_vec)
    print(f"--- {name} ---")
    print(classification_report(y_test, y_pred))
    
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=model.classes_, yticklabels=model.classes_)
    plt.title(f"Matrice de confusion - {name}")
    plt.xlabel("Prédictions")
    plt.ylabel("Vérités")
    plt.tight_layout()
    plt.show()


def main():
    # Chargement et préparation des données
    df = load_data()
    X_train, X_test, y_train, y_test = split_data(df)

    # Debug : dimensions des jeux de données
    print(f"X_train shape: {X_train.shape}")
    print(f"X_test shape: {X_test.shape}")

    # Vectorisation TF-IDF
    X_train_vec, X_test_vec, vectorizer = vectorize_text(X_train, X_test)

    # Dictionnaire des modèles à tester
    models = {
        "Naive Bayes": MultinomialNB(),
        "SVM": SVC(),
        "Random Forest": RandomForestClassifier()
    }

    # Entraînement et évaluation de chaque modèle
    for name, model in models.items():
        model.fit(X_train_vec, y_train)
        evaluate_model(name, model, X_test_vec, y_test)


if __name__ == "__main__":
    main()









