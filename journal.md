# Journal de Projet — Fouille de Texte

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


