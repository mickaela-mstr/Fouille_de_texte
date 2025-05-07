# Journal de branche April 27 - Création de corpus

### Objectif 
- Utiliser des sources fiables pour sélectionner des titres représentatifs du genre
- Construire un corpus de paroles de chansons pour le genre R&B
- Utiliser l'API Genius pour récupérer automatiquement les paroles

### Actions réalisées
- Création d'un compte Genius.
- Génération d'un Access Token: [https://genius.com/api-clients](https://genius.com/api-clients).
- Mise en place d'un premier script Python avec `lyricsgenius` pour interroger l'API.
- Adjustement de paramètres de sécurité dans l'API (timeouts, retries)
- Préparer un environnement de travail propre pour le projet
- Installer la bibliothèque `lyricsgenius` pour récupérer les paroles de chansons

- Recherche de chansons R&B populaires et influentes.
- Utilisation de deux sources principales :
  - Rolling Stone — Best R&B Songs of the 21st Century: <br> https://www.rollingstone.com/music/music-lists/best-rnb-songs-21st-century-1234878625/the-internet-special-affair-1234878878/
  - Spotify — Greatest R&B Songs of the Streaming Era: <br> https://newsroom.spotify.com/2024-04-09/greatest-rnb-songs-classics-streaming-era/

- Sélection d'une centaine de titres d'artistes majeurs 
- Formatage correct des paires (titre, artiste) pour utilisation dans un script Python

### Problèmes rencontrés
- Certains titres comportaient des erreurs de formatage (guillemets incorrects, virgules manquantes)
- Remplacement des guillemets typographiques (“ ”) par des guillemets droits (" ").
- Ajout systématique de virgules à la fin de chaque tuple (titre, artiste).

### Prochaines étapes
- Vérifier quels morceaux n'ont pas pu être récupérés et les remplacer si besoin
- Commencer la vectorisation des fichiers `.txt` en `.arff` pour Weka

# Journal de branche May 7 — Synchronisation Git & Évaluation des Modèles

## Synchronisation du corpus entre branches Git
- **Import du dossier `corpus/`** depuis la branche `micka_branche_1` sans tout fusionner :
  ```bash
  git checkout micka_branche_1 -- corpus/
  ```
  faire la même chose pour recuperer vectorisation.py de la branche principale dans jourdan_branche1
  
## Préparation d’un jeu de test « held-out » (20 %)
1. **Répartition aléatoire** (80 % train / 20 % test) avec `split_and_shuffle.py`  
   ```bash
   python3 shuffle_and_split.py
   # → création de corpus_train/ et corpus_test/
   ```  
2. **Vectorisation du train** (_vocabulaire_) :  
   ```bash
   python3 scripts/vectorisation.py corpus_train/ train.arff
   ```  
3. **Vectorisation du test** (même vocabulaire) :  
   ```bash
   python3 scripts/vectorisation.py --lexicon train.arff corpus_test/ test.arff
   ```  
4. **Évaluation dans Weka** :  
   - Ouvrir **train.arff** → onglet Classify  
   - Test options → **Supplied test set** → charger **test.arff**  
   - Choisir l’algorithme (NaiveBayes, SMO, J48…) → **Start**

## Cross-validation 10-fold (sans split manuel)
- **Vectoriser tout le corpus** en un seul fichier ARFF :  
  ```bash
  python3 scripts/vectorisation.py corpus_clean/ all_data.arff
  ```  
- Dans Weka : Test options → **Cross-validation** → 10 folds → **Start**

## Comparaison et méthodologie “2-en-1”
1. **Cross-validation** sur `all_data.arff` pour un benchmark rapide et une estimation moyenne.  
2. **Held-out + lexicon partagé** :  
   - Split 80/20 → `train.arff` / `test.arff`  
   - CV dans Weka sur **train.arff** pour le tuning hyper-paramétrique  
   - Évaluation finale sur **test.arff** pour mesurer la généralisation  
3. **Documentation** dans le rapport :  
   - Scores CV vs scores held-out  
   - Tableau de comparaison (accuracy, F1-score, matrice de confusion)  
   - Discussion des écarts (sur-apprentissage, impact du prétraitement, etc.)

> **Avancement :**  
> - Synchronisation Git et import du corpus terminés.  
> - Scripts de split & vectorisation prêts.  
> - Prochaines étapes : 
>   - Lancer les deux workflows (CV & held-out)  
>   - Collecter les résultats et rédiger la section “Expériences” du rapport.

