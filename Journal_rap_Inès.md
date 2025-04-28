# Journal de suivi des avancées pour la partie rap - Inès

## Création et tests de plusieurs scripts indépendants :

### songs_lyrics_rap.py :
- Permet de mettre les paroles (lyrics) des chansons (songs) sélectionnées dans des fichiers textes indépendants nommés selon le format suivant : artiste_titre.txt
- Ce programme nécessite qu'on lui donne une liste de titres (rap_songs) au format suivant : ("titre", "artiste"), ce que je vais chercher à automatiser avec le programme suivant.
- Testé sur une liste de cinq titres de rap aléatoires donnés par l'utilisateur.

### songs_titles_rap.py :
- Permet de créer la liste de titres (rap_songs) demandée par le programme précédent, pour les tests il a été plus simple de les créer et tester indépendamment.
- Ce programme nécessite qu'on lui donne le nom des artistes afin de chercher leurs titres les plus populaires (nombre de chansons demandé par l'utilisateur), ce que je vais de nouveau chercher à automatiser dans un nouveau programme.
- Testé sur une liste d'artistes de rap aléatoire donnés par l'utilisateur.

### songs_artists_rap.py :
- Le scrapping pour le nom des artistes est beaucoup plus complexe car l'API de genius renvoie des noms d'artistes aléatoires et ne peut donc pas être utilisé.
- J'ai tenté de scrapper les noms directement sur Wikipédia mais les informations renvoyées ne sont pas ce que j'attends.

### scrap_rap.py :
- Assemblage des deux premiers scripts indépendants qui fonctionnent bien su'ils prennent énormément de temps. Si j'arrive à faie fonctionner correctement ```songs_artists_rap.py``` je complèterai éventuellement ce script plus tard afin qu'il puisse scrapper les données des artistes, des titres et des paroles automatiquement de A à Z.

## Dépot du "corpus_rap" obtenu avec ```scrap_rap.py``` :
- Le corpus créé à partir du script précédent est déposé sur le git pour pouvoir être utilisé pour la suite.
