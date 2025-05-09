# Classification de chansons par genre à partir des paroles

Projet de fouille de texte (LZT001 – M1 TAL)
Sorbonne Nouvelle, 2024-2025

## Description

Ce projet a pour objectif de classifier automatiquement des chansons par genre musical (rap, pop, R\&B) en analysant uniquement leurs paroles. Le modèle ne dispose ni de la musique ni de métadonnées : il se base exclusivement sur le contenu lexical des textes.

Nous avons constitué un corpus équilibré de 453 chansons en anglais, puis appliqué des techniques de prétraitement, vectorisation, analyse exploratoire et classification supervisée à l’aide de la bibliothèque scikit-learn (et Weka pour comparaison).

---

## Contenu du dépôt

```
.
├── corpus/                      # Fichiers textes bruts par genre (pop, rap, rnb)
├── resultats_weka/              # Dossier avec les résultats de weka
├── resultats_python/
│   ├── wordcloud_pop.png        # Nuage de mots du genre pop
│   ├── wordcloud_rap.png        # Nuage de mots du genre rap
│   ├── wordcloud_rnb.png        # Nuage de mots du genre rnb
│   ├── nb.png                   # Matrice de confusion Naive Bayes
│   ├── svm.png                  # Matrice de confusion SVM
│   ├── rf.png                   # Matrice de confusion Random Forest
│   ├── compare_3.png            # Les 3 matrices côte à côte
│   ├── compare_accuracies.png   # Accuracy des modèles (GridSearch)
│   └──  compare_random_state.png # Accuracy moyenne ± écart-type (multi-runs)
├── tableaux/
│   ├── resultats_gridsearch.csv
│   ├── perf_modeles.csv
│   └── lyrics.csv               # Corpus nettoyé prêt à être utilisé
├── scripts/
    ├── shuffle_and_split.py
│   ├── recup_paroles.py         # Récupération des paroles (API Genius)
│   ├── data_prep.py             # Nettoyage + génération de lyrics.csv
│   ├── nuage_mot.py             # Wordclouds par genre
│   ├── algo.py                  # Classification + GridSearch + évaluation
│   ├── plot_scores.py           # Comparaison des accuracies (barplot)
│   └── plot_random_state.py     # Barplot avec erreurs (multi-runs)
├── Rapport Fouille de texte.pdf
└── README.md

```

---

## 🚀 Lancer une classification

Lancer le script principal de classification (avec GridSearchCV + évaluation) :

```bash
python3 scripts/algo.py
```

---

## Résultats

* SVM (noyau linéaire) obtient les meilleurs résultats globaux avec une accuracy de 66 %.
* Naive Bayes et Random Forest atteignent environ 60 %, avec des comportements très différents :

  * Naive Bayes est plus stable mais confond pop et R\&B.
  * Random Forest distingue bien rap et R\&B mais échoue sur la pop.
* Le genre rap est plus facilement identifiable, tandis que pop et R\&B sont lexicalement très proches.
* Les résultats sont confirmés par :

  * les matrices de confusion,
  * les rapports de classification,
  * les graphes de performance,
  * et les nuages de mots.

---

## Bibliographie

* [Scikit-learn Documentation](https://scikit-learn.org/stable/)
* [Genius API Docs](https://docs.genius.com/)
* [Weka Wiki](https://waikato.github.io/weka-wiki/)
* Cours "Introduction à la fouille de texte" – Yoann Dupont / Isabelle Tellier & Loïc Grobol

---

## Auteurs

* Inès Martins — [GitHub](https://github.com/Inesmartins1912)
* Mickaëla Mastrodicasa — [GitHub](https://github.com/mickaela-mstr)
* Jourdan Wilson — [GitHub](https://github.com/jourdanwilson)
