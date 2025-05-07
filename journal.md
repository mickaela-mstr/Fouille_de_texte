# Journal de bord de micka:

## Constitution du corpus:

Pour constituer le corpus de travail utilisé dans le projet, j'ai crée un script Python `recup_parole.py`  afin de récupérer automatiquement les paroles de chansons à partir de l’API Genius. Cette API permet d’accéder aux paroles de titres musicaux en interrogeant soit un artiste donné, soit des combinaisons titre/artiste précises.

Deux modes d’utilisation sont prévus : le premier permet d’obtenir les chansons les plus populaires d’un artiste donné, en utilisant la fonction `get_artist_songs()`. Cette fonction interroge l’API en fournissant le nom de l’artiste, et renvoie une liste de chansons sous forme de paires `(titre, artiste)`. L’utilisateur peut choisir l’artiste à interroger grâce à un argument en ligne de commande (`--artist`) et préciser le genre associé (`--genre`, par exemple "rap", "pop", "r\&b").

Une fois la liste des chansons obtenue, `searchbysongs()`, va interroger Genius chanson par chanson. Pour chaque titre, elle télécharge les paroles si elles sont disponibles, puis les enregistre dans un fichier texte avec `savesong()`. Cette dernière sauvegarde les fichiers sous le nom `<artiste>_<titre>.txt`.

Le script utilise également `argparse` pour choisir l'artiste en ligne de commande. Il est possible de l’exécuter avec une commande comme :

```bash
python3 recup_parole.py --artist "21 Savage" --genre rap
```

## Prétraitement des données :

Dans le cadre de ce projet, l’objectif était de construire un jeu de données propre et structuré à partir de fichiers texte contenant les paroles de chansons issues de trois genres musicaux : le rap, la pop et le RnB. Ces données devaient être préparées en vue d’une tâche de classification automatique selon le genre musical.

Pour cela, un corpus de fichiers `.txt` a été constitué, organisé dans trois dossiers distincts (`corpus/rap`, `corpus/pop`, `corpus/rnb`). Chaque fichier contenait les paroles d’une chanson, mais également diverses informations parasites telles que les noms des contributeurs, les liens vers des traductions, des résumés, ou encore des métadonnées générées par les plateformes de lyrics. Le premier enjeu a donc été de filtrer ces fichiers pour en extraire uniquement les véritables paroles.

Un script Python `data_prep.py` a été développé pour automatiser cette étape de prétraitement. À l’aide du module `glob`, les fichiers ont été récupérés dans chaque dossier et organisés dans un dictionnaire par genre. Une fonction principale, `get_table()`, a ensuite été chargée de lire chaque fichier, d’y appliquer un nettoyage ciblé, puis de stocker les résultats dans un fichier CSV.

Le nettoyage du texte a été confié à la fonction `clean_lyrics()`. Cette dernière avait pour rôle d’ignorer toutes les lignes de texte inutiles en amont des paroles, et de supprimer les balises comme `[Verse]`, `[Chorus]`, `[Bridge]`, etc. Cependant, avec les fichiers du genre rap, contrairement aux morceaux pop ou RnB, on avaient très rarement ces balises. Et ils incluaient presque systématiquement une première ligne non pertinente (contributeurs, tags de plateforme, etc.). Pour remédier à cela, une exception a été ajoutée dans le script : la première ligne de chaque fichier de rap est systématiquement supprimée avant tout traitement.

Une fois les paroles nettoyées, elles ont été enregistrées dans un fichier CSV avec trois colonnes : `Parole` (le texte nettoyé), `Genre` (le genre musical), et `Titre + artiste` (le nom original du fichier `.txt`, permettant d’identifier la chanson). Ce fichier constitue désormais un jeu de données propre, prêt à être utilisé pour des étapes d’analyse exploratoire ou d’apprentissage automatique.


### Premier test d'algo de classification : Analyse des résultats du modèle Random Forest

#### Objectif

L'objectif de ce script était de tester un algorithme d'apprentissage supervisé our classer automatiquement des paroles de chansons en trois genres musicaux.

#### Prétraitement

Les paroles ont été vectorisées à l’aide de la méthode TF-IDF, qui pondère les termes selon leur fréquence dans un document et leur rareté dans l’ensemble du corpus.

#### Modèle entraîné

Le modèle utilisé est un RandomForestClassifier de scikit-learn, un classifieur d'ensemble basé sur des arbres de décision.

#### Résultats – matrice de confusion

La matrice (dans le dossier matrices) montre, pour chaque genre réel (ligne), combien d’exemples ont été classés dans chaque genre prédit (colonne).

* Rap : Le modèle a correctement classé 25 chansons sur 30 comme rap, avec seulement 5 erreurs. C’est la classe la mieux reconnue, ce qui peut s’expliquer par une plus grande spécificité lexicale ou structurelle des textes rap (vocabulaire plus argotique ou direct, phrases plus longues…).

* Pop : Résultats mitigés. Seules 10 chansons pop ont été bien classées, tandis que **19** ont été classées à tort comme rnb. Cela suggère une forte confusion entre ces deux genres, peut-être liée à des similitudes thématiques (amour, émotions) ou lexicales.

* Rnb : Le modèle a correctement identifié 26 chansons sur 37, avec des confusions notables vers pop (8 erreurs) et un peu vers **rap** (3 erreurs). Comme pour la pop, cette confusion avec pop pourrait être due à un lexique commun ou à des structures de phrases proches.

#### Hypothèses

* La confusion entre **pop** et **rnb** pourrait être réduite en :

  * Utilisant des n-grammes (plutôt que des mots seuls) dans le `TfidfVectorizer`
  * Ajoutant un filtrage lexical pour retirer les mots trop fréquents ou non discriminants (`max_df`, `min_df`)
  * Introduisant une analyse sémantique plus riche (lemmatisation, entités, thèmes, etc.)


