# Fouille de Texte — Classification de Chansons par Genre

## Description
Projet universitaire de fouille de texte visant à prédire le genre musical d'une chanson à partir de ses paroles.

## Objectif
- Construire un corpus de chansons triées par genre (R&B, Pop, Rap)
- Prétraiter et nettoyer les textes
- Vectoriser les paroles en représentations numériques (ARFF)
- Entraîner et comparer plusieurs modèles de classification (Naive Bayes, SVM)
- Évaluer la précision de la prédiction automatique/ la capacité de généralisation des modèles

## Organisation du dépôt

```
Fouille_de_texte/
├── corpus/                      # Paroles brutes classées par genre
├── corpus_train/                # 80% des données pour l'entraînement
├── corpus_test/                 # 20% des données pour le test final
├── scr/                          # Scripts de traitement
│   ├── scraper_script.py        # Récupération des paroles via Genius
│   ├── preprocess_corpus.py     # Nettoyage léger (balises, ponctuation, stop-words)
│   ├── split_and_shuffle.py     # Répartition aléatoire train/test
│   └── vectorisation.py         # Génération des fichiers ARFF pour Weka
├── song_list_rnb.txt            # Liste des titres et artistes R&B utilisés
├── weka_.arff_files/            # Fichiers ARFF générés
├── results/                     # Résultats Weka (.txt et .arff) 
├── journal.md                   # Carnet de bord des étapes, problèmes et ressources
└── README.md                    # Présentation du projet
```

## Utilisation

1. **Récupération des paroles** (exemple pour R&B) :
```bash
 python3 scripts/scraper_script.py
```
Les fichiers `.txt` seront générés sous `corpus/<genre>/`.

2. **Nettoyage** :
```bash
 python3 scripts/preprocess_corpus.py corpus/ corpus_clean/ --remove-stopwords
```

3. **Répartition train/test** :
```bash
 python3 scripts/split_and_shuffle.py
```
→ `corpus_train/` & `corpus_test/` sont créés.

4. **Vectorisation** :
- **Sur l’ensemble pour CV** :
```bash
 python3 scripts/vectorisation.py corpus/ all_data.arff
```
- **Held-out train/test** :
```bash
 python3 scripts/vectorisation.py corpus_train/ train.arff
 python3 scripts/vectorisation.py --lexicon train.arff corpus_test/ test.arff
```

5. **Classification et évaluation dans Weka** :
- CV 10-fold sur `all_data.arff` (Test options → Cross-validation)
- Supplied test set (`test.arff`) pour le test final (Test options → Supplied test set)

## Méthodologie

1. **Corpus** : collecte via Genius + liste de 50 titres R&B (voir `song_list_rnb.txt`).
2. **Journalisation** : suivi quotidien des problèmes, solutions et sources (Rolling Stone, Spotify).
3. **Prétraitement** : suppression des balises, passage en minuscules, retrait de la ponctuation, option stop-words.
4. **Évaluation** : comparaison cross-validation vs held-out pour mesurer impact du prétraitement et qualité du modèle.

## Technologies

- Python 3
- LyricsGenius API
- Weka (ARFF, NaiveBayes, J48, SMO, RandomForest, IBK)
- Git & GitHub



