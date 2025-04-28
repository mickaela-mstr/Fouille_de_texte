# Fouille de Texte — Classification de Chansons par Genre

## Description
Projet universitaire de fouille de texte visant à prédire le genre musical d'une chanson à partir de ses paroles.

## Objectif
- Construire un corpus de chansons triées par genre (R&B, Pop, Rap)
- Vectoriser les paroles en représentations numériques
- Entraîner des modèles de classification (Naive Bayes, SVM)
- Évaluer la précision de la prédiction automatique

## Organisation
- `README.md` — Présentation générale du projet
- `journal.md` — Journal de bord retraçant la progression personnelle dans le projet
- `corpus_rap` — Corpus composé des textes étant les paroles des chansons du genre rap
- `songs_titles.py` — Script utilisant l'API Genius pour sélectionner les titres de chansons pour le genre rap
- `songs_lyrics.py` — Script utilisant l'API Genius pour sélectionner le contenu textuel des paroles des chansons pour le genre rap
- `scrap_rap.py` — Script final pour récupérer automatiquement les paroles via l'API Genius
- `corpus_rap` — Corpus composé des textes étant les paroles des chansons du genre rap

## Technologies
- Python 3
- LyricsGenius API
- Weka
- Git, GitHub
