"""
Script utiliser pour tester différrents algorithmes de classification sur nos données.
"""

import csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.svm import SVC
from sklearn.utils import shuffle
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


def load_data(csv_path="lyrics.csv"):
    """chargement des données"""
    
    df = pd.read_csv(csv_path)
    return df

def split_data(df):
    """split les données en jeu d'entraînement et de test"""
    X = df.drop(columns=["Genre"])
    y = df["Genre"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    
    print(f"X_train shape: {X_train.shape}")
    print(f"X_test shape: {X_test.shape}")
    print(X_train)

    return train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

def vectorize_text(X_train, X_test, text_column="Parole"):
    """vectorise les textes avec TF-IDF"""
    vectorizer = TfidfVectorizer()
    X_train_vec = vectorizer.fit_transform(X_train[text_column])
    X_test_vec = vectorizer.transform(X_test[text_column])

    return X_train_vec, X_test_vec, vectorizer


def evaluate_model(name, model, X_test_vec, y_test):
    """affiche le rapport de classification et la matrice de confusion"""
    y_pred = model.predict(X_test_vec)
    acc = accuracy_score(y_test, y_pred)

    print(f" {name} ")
    print(f"Accuracy : {acc:.2f}")
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

def plot_confusion_matrices(models, model_names, X_test_vec, y_test):
    """affiche les matrices de confusion de plusieurs modèles côte à côte"""
    
    n = len(models)
    fig, axes = plt.subplots(1, n, figsize=(6 * n, 5))

    if n == 1:
        axes = [axes]

    for i, (model, name) in enumerate(zip(models, model_names)):
        y_pred = model.predict(X_test_vec)
        cm = confusion_matrix(y_test, y_pred)
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=axes[i],
                    xticklabels=model.classes_, yticklabels=model.classes_)
        axes[i].set_title(f"{name}")
        axes[i].set_xlabel("Prédiction")
        axes[i].set_ylabel("Vérité")

    plt.tight_layout()
    plt.show()

def multi_run_evaluation(df, best_nb, best_svm, best_rf, n_runs=10):
    
    results = {
        "Naive Bayes": [],
        "SVM": [],
        "Random Forest": []
    }

    for seed in range(1, n_runs + 1):
        # split aléatoire
        X = df.drop(columns=["Genre"])
        y = df["Genre"]
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=seed, stratify=y)

        # Vectorisation
        X_train_vec, X_test_vec, _ = vectorize_text(X_train, X_test)

        # Évaluations
        for name, model in zip(results.keys(), [best_nb, best_svm, best_rf]):
            model.fit(X_train_vec, y_train)
            y_pred = model.predict(X_test_vec)
            acc = accuracy_score(y_test, y_pred)
            results[name].append(acc)

    # Résumé des perfs
    with open("perf_modeles.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Modèle", "Accuracy moyenne", "Écart-type"])
        for name, scores in results.items():
            mean_acc = np.mean(scores)
            std_acc = np.std(scores)
            writer.writerow([name, f"{mean_acc:.4f}", f"{std_acc:.4f}"])
            print(f"{name}: Accuracy moyenne = {mean_acc:.4f} | Écart-type = {std_acc:.4f}")

def main():

    # chargement et préparation des données
    df = load_data()
    X_train, X_test, y_train, y_test = split_data(df)

    # vectorisation TF-IDF
    X_train_vec, X_test_vec, vectorizer = vectorize_text(X_train, X_test)

    # liste pour stocker les scores
    results = []

    ### GridSearch pour NB
    nb_param_grid = {'alpha': [0.1, 0.5, 1.0]}
    nb = MultinomialNB()
    nb_grid = GridSearchCV(estimator=nb, param_grid=nb_param_grid,
                           scoring='accuracy', cv=5, n_jobs=-1, verbose=1)
    nb_grid.fit(X_train_vec, y_train)
    best_nb = nb_grid.best_estimator_
    print(">>> Naive Bayes best parms:", nb_grid.best_params_)

    # Évaluation finale
    acc_nb = accuracy_score(y_test, best_nb.predict(X_test_vec))
    results.append(["Naive Bayes", acc_nb, nb_grid.best_params_])
    evaluate_model("Naive Bayes (mais mieux)", best_nb, X_test_vec, y_test)

    ### GridSearch pour SVM 
    svm_param_grid = {
        'kernel': ['linear', 'rbf'],
        'C': [0.1, 1, 10]
    }
    svm = SVC()
    svm_grid = GridSearchCV(estimator=svm, param_grid=svm_param_grid,
                            scoring='accuracy', cv=5, n_jobs=-1, verbose=1)
    svm_grid.fit(X_train_vec, y_train)
    best_svm = svm_grid.best_estimator_
    print(">>> SVM best parms:", svm_grid.best_params_)

    acc_svm = accuracy_score(y_test, best_svm.predict(X_test_vec))
    results.append(["SVM", acc_svm, svm_grid.best_params_])
    evaluate_model("SVM (mais mieux)", best_svm, X_test_vec, y_test)

    ### GridSearch pour Random Forest
    rf_param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5]
    }
    rf = RandomForestClassifier(random_state=42)
    rf_grid = GridSearchCV(estimator=rf, param_grid=rf_param_grid,
                           scoring='accuracy', cv=5, n_jobs=-1, verbose=1)
    rf_grid.fit(X_train_vec, y_train)
    best_rf = rf_grid.best_estimator_
    print(">>> Random Forest best parms:", rf_grid.best_params_)

    acc_rf = accuracy_score(y_test, best_rf.predict(X_test_vec))
    results.append(["Random Forest", acc_rf, rf_grid.best_params_])
    evaluate_model("Random Forest (mais mieux)", best_rf, X_test_vec, y_test)

    with open("resultats_gridsearch.csv", mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Modèle", "Accuracy", "Meilleurs paramètres"])
        for model_name, acc, params in results:
            writer.writerow([model_name, f"{acc:.4f}", str(params)])

    all_models = [best_nb, best_svm, best_rf]
    all_names = ["Naive Bayes (mais mieux)", "SVM (mais mieux)", "Random Forest (mais mieux)"]
    plot_confusion_matrices(all_models, all_names, X_test_vec, y_test)

    multi_run_evaluation(df, best_nb, best_svm, best_rf)

if __name__ == "__main__":
    main()









