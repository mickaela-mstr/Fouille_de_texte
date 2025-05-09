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


## Premier test d'algo de classification : Analyse des résultats du modèle Random Forest

### Objectif

L'objectif de ce script était d'appréhender et tester un algorithme d'apprentissage supervisé our classer automatiquement des paroles de chansons en trois genres musicaux.

### Prétraitement

Les paroles ont été vectorisées à l’aide de la méthode TF-IDF, qui pondère les termes selon leur fréquence dans un document et leur rareté dans l’ensemble du corpus.

### Modèle entraîné

Le modèle utilisé est un RandomForestClassifier de scikit-learn, un classifieur d'ensemble basé sur des arbres de décision.

### Résultats – matrice de confusion

La matrice (dans le dossier matrices) montre, pour chaque genre réel (ligne), combien d’exemples ont été classés dans chaque genre prédit (colonne).

* Rap : Le modèle a correctement classé 25 chansons sur 30 comme rap, avec seulement 5 erreurs. C’est la classe la mieux reconnue, ce qui peut s’expliquer par une plus grande spécificité lexicale ou structurelle des textes rap (vocabulaire plus argotique ou direct, phrases plus longues…).

* Pop : Résultats mitigés. Seules 10 chansons pop ont été bien classées, tandis que 19 ont été classées à tort comme rnb. Cela suggère une forte confusion entre ces deux genres, peut-être liée à des similitudes thématiques (amour, émotions) ou lexicales.

* Rnb : Le modèle a correctement identifié 26 chansons sur 37, avec des confusions notables vers pop (8 erreurs) et un peu vers rap (3 erreurs). Comme pour la pop, cette confusion avec pop pourrait être due à un lexique commun ou à des structures de phrases proches.

### Hypothèses

* La confusion entre pop et rnb pourrait être réduite en :

  * Utilisant des n-grammes (plutôt que des mots seuls) dans le `TfidfVectorizer`
  * Ajoutant un filtrage lexical pour retirer les mots trop fréquents ou non discriminants (`max_df`, `min_df`)
  * Introduisant une analyse sémantique plus riche (lemmatisation, entités, thèmes, etc.)

## Tests avec les autres algos et prises en compte des hyperparamètres

### Prise en main des hyperparamètres

Les données ont été divisées en deux sous-ensembles : un ensemble d’entraînement représentant 70 % du corpus total, et un ensemble de test représentant les 30 % restants. Ce découpage a été effectué à l’aide de la fonction `train_test_split` de `scikit-learn`, en veillant à maintenir la proportion des classes (rap, pop, rnb) dans chaque sous-ensemble grâce à l’argument `stratify`. C'est pour que l’évaluation du modèle ne soit pas faussée par une répartition déséquilibrée des genres musicaux dans les jeux de données.

Comme pour le premier test, avant l’entraînement des modèles, les paroles de chansons ont été vectorisées à l’aide de TF-IDF (`TfidfVectorizer`).

Naive Bayes, SVM et Random Forest sont les algos sélectionnés pour la tâche de classification. Cependant, chaque modèle comporte des hyperparamètres qui influencent fortement son comportement et sa capacité de généralisation. Afin de sélectionner les meilleures combinaisons de paramètres pour chaque algorithme, nous avons utilisé un outil fourni par `scikit-learn` : `GridSearchCV`.

La méthode `GridSearchCV` permet de tester automatiquement un ensemble de combinaisons d’hyperparamètres et de sélectionner celle qui maximise une métrique de performance (ici, l’accuracy), en utilisant une validation croisée à 5 plis (5-fold cross-validation). Concrètement, les données d’entraînement sont elles-mêmes divisées en cinq sous-ensembles : à chaque itération, le modèle est entraîné sur quatre d’entre eux et évalué sur le cinquième. Ce processus est répété cinq fois, ce qui permet d’évaluer la robustesse du modèle tout en évitant les biais dus à un découpage unique.

#### NB

Pour Naive Bayes, nous avons testé différentes valeurs du paramètre de lissage `alpha` : 0.1, 0.5 et 1.0. Le modèle Naive Bayes est basé sur des probabilités : il estime pour chaque mot sa probabilité d’apparaître dans chaque classe (ici, chaque genre musical). Mais il arrive qu’un mot présent dans une chanson du test ne soit jamais apparu dans les chansons du corpus d'entraînement. Dans ce cas, sa probabilité est considérée comme nulle, ce qui peut faire chuter la probabilité globale de la classe, même si le reste du texte est très représentatif.

Pour résoudre ce problème, on utilise un lissage appelé lissage de Laplace, qui consiste à ajouter artificiellement une petite probabilité à tous les mots, même ceux qu’on n’a jamais vus pendant l’apprentissage. Cela évite les zéros dans les calculs. Ce lissage est contrôlé par un paramètre alpha : Si alpha est petit (ex: 0.1), on ajoute une petite quantité de probabilité fictive i.e le modèle reste très sensible aux mots rares. Si alpha est grand (ex: 1.0), on ajoute plus de probabilité à tous les mots i.e le modèle devient plus “conservateur” et moins influencé par les mots rares.

Dans notre expérimentation, nous avons testé plusieurs valeurs de alpha pour trouver le bon équilibre entre spécificité (mots rares) et généralisation. Cela nous permet de voir si un modèle très sensible au lexique est plus performant qu’un modèle plus lissé.

#### SVM

Pour SVM, nous avons utilisé le type de noyau (`kernel`) et le paramètre de régularisation `C`. Le noyau est une fonction mathématique qui permet au modèle de tracer une frontière de séparation entre les classes (ici : rap, pop, rnb) dans l’espace vectoriel défini par les représentations TF-IDF des chansons.

Nous avons testé deux types de noyaux : le noyau linéaire (`kernel="linear"`) et le noyau RBF (`kernel="rbf"` pour Radial Basis Function). Le noyau linéaire suppose que les classes peuvent être séparées par un hyperplan, c’est-à-dire une “ligne droite” dans un espace multidimensionnel. Ce type de noyau fonctionne bien avec les données textuelles, car les représentations TF-IDF vivent déjà dans des espaces de très grande dimension, où les classes sont souvent naturellement séparables. Le noyau linéaire présente également l’avantage d’être rapide à entraîner et de limiter les risques de surapprentissage.

Le noyau RBF, en revanche, permet une séparation non linéaire : il est capable de tracer des frontières de décision plus flexibles, en courbe, pour mieux épouser la forme des données. Cela peut être utile lorsque les classes ne sont pas bien séparées dans l’espace initial. Toutefois, ce noyau est plus coûteux en calcul, et surtout plus sensible à l'overfitting, c’est-à-dire au risque de trop bien s’ajuster aux exemples d’entraînement sans bien généraliser.

Aussi, nous avons testé différentes valeurs du paramètre `C`, qui contrôle la régularisation du modèle. Un faible `C` (par exemple 0.1) indique au modèle qu’il peut tolérer quelques erreurs de classification sur les données d’entraînement, en échange d’une frontière de séparation plus simple. À l’inverse, un grand `C` (comme 10) demande au modèle de minimiser au maximum les erreurs, quitte à créer une frontière plus complexe, ce qui peut améliorer la précision à court terme, mais parfois au détriment de la généralisation.

#### Arbre de décision (random forest)

Pour Random Forest, nous avons testé les combinaisons suivantes : nombre d’arbres (`n_estimators` de 100 à 200). Un plus grand nombre d’arbres permet généralement de lisser les prédictions et de mieux généraliser, mais au prix d’un temps de calcul plus long. 100 est souvent un bon point de départ, tandis que 200 permet de vérifier si la performance continue à s’améliorer ou si elle se stabilise.

Il y a aussi la profondeur maximale des arbres (`max_depth` : None, 10, 20). Lorsqu’il est fixé à None, chaque arbre peut continuer à croître tant qu’il trouve des subdivisions possibles dans les données. Cela permet une modélisation très fine, mais peut aussi entraîner un surapprentissage. En testant également des profondeurs limitées (10 et 20), nous cherchons à contraindre la complexité du modèle pour qu’il reste plus simple et plus généralisable.

Et enfin la taille minimale des sous-ensembles qui définit le nombre minimum d’échantillons requis pour diviser un nœud. Si ce nombre est trop bas (ex : 2), les arbres peuvent se subdiviser de manière excessive, créant des règles trop spécifiques. En augmentant cette valeur à 5, on force l’arbre à regrouper un peu plus d’exemples avant de se diviser pour effectuer une division (`min_samples_split` : 2 ou 5).

Une fois la recherche par grille effectuée pour chaque algorithme, nous avons entraîné les meilleurs modèles trouvés (`best_estimator_`) sur l’ensemble d’entraînement. Chaque modèle a ensuite été évalué sur le jeu de test à l’aide de plusieurs indicateurs : l’accuracy, la matrice de confusion, ainsi qu’un rapport de classification affichant la précision, le rappel et le F1-score pour chaque classe.

### Évaluation des perfs des modèles : multi-exécutions avec variations aléatoires

#### Random state

Après avoir sélectionné les meilleurs hyperparamètres pour chaque modèle, il est nécessaire de vérifier que les performances observées ne sont pas simplement dues au hasard d’un découpage particulier des données. Pour cela, nous avons mis en place une évaluation par validation multi-runs, qui consiste à :

* Répéter plusieurs fois le processus d’entraînement et d’évaluation,
* En variant le `random_state` utilisé pour le découpage des données en jeu d'entraînement et de test,
* Et en mesurant à chaque fois l'accuracy des modèles sur un test indépendant.

Nous avons défini une fonction `multi_run_evaluation()` qui prend en entrée :

* Le DataFrame contenant les données (`df`),
* Les meilleurs modèles (`best_nb`, `best_svm`, `best_rf`) trouvés via `GridSearchCV`,
* Et le nombre de répétitions souhaité (`n_runs`, fixé ici à 10).

À chaque exécution, le processus est le suivant :

1. Nouveau split aléatoire du corpus en 70 % entraînement et 30 % test, avec un `random_state` différent à chaque itération.
2. Vectorisation TF-IDF des paroles.
3. Réentraînement de chaque modèle sur ce nouveau jeu d'entraînement.
4. Prédiction sur le jeu de test, et calcul de l’accuracy obtenue.

### Résultats : Interprétation des matrices de confusion

#### NB

Le modèle Naive Bayes montre une nette tendance à confondre les chansons pop avec le genre rnb. En effet, sur 46 chansons réellement de genre pop, seules 11 sont correctement classées comme telles, tandis que 32 sont classées à tort comme rnb. Cette confusion s’observe également, dans une moindre mesure, pour le genre rap : 14 chansons rap sont elles aussi mal étiquetées en rnb. En revanche, le modèle reconnaît assez bien les chansons rnb, avec 48 prédictions correctes sur 55. Ce comportement s’explique sans doute par le manque de sensibilité aux structures globales du texte ou aux cooccurrences complexes de termes, ce qui peut nuire à sa capacité à distinguer des genres proches lexicalement.

#### SVM

Le modèle SVM présente une amélioration notable. Il reconnaît bien les chansons pop (25 sur 46) et montre une bonne capacité à classifier les chansons rap (32 sur 45). Comme pour Naive Bayes, la principale source d’erreurs se situe entre pop et rnb, avec 20 chansons pop classées comme rnb, et 13 chansons rnb prédites comme pop. Toutefois, la séparation entre rap et les deux autres genres est bien plus nette qu’avec Naive Bayes. Ce résultat confirme que le SVM, surtout avec un noyau linéaire, est bien adapté aux représentations TF-IDF, car il exploite efficacement la géométrie de l’espace vectoriel pour tracer des frontières de décision claires.

#### Random Forest

Le modèle Random Forest affiche les meilleures performances en ce qui concerne la classification des genres rap et rnb. Il parvient à identifier 34 chansons rap sur 45, et 51 chansons rnb sur 55, ce qui représente une excellente précision pour ces deux classes. Cependant, il échoue presque totalement sur la classe pop, avec seulement 3 bonnes prédictions. La quasi-totalité des chansons pop (40 sur 46) sont classées à tort comme rnb. Cette défaillance peut s’expliquer par un surapprentissage du modèle sur certaines caractéristiques lexicales propres au rnb, qui pourraient aussi apparaître dans les chansons pop, rendant la frontière entre ces deux genres trop fine pour être bien capturée par les arbres de décision.

#### Hypothèses

La confusion entre pop et rnb peut s’expliquer par un lexique commun. Ces deux genres partagent souvent les mêmes thèmes et le même registre de langage. Le rap est mieux séparé car son vocabulaire est plus spécifique. Pour améliorer les performances, il est possible d’ajouter une lemmatisation, d’utiliser des n-grammes, d’appliquer une pondération des classes ou d’intégrer des représentations plus riches comme les embeddings. Il serait également utile de rééquilibrer le corpus, notamment en augmentant la présence de chansons pop.

### Résultats: Interprétation du rapport de classification et des accuracies

Les résultats montrent que le modèle SVM obtient la meilleure performance globale avec une accuracy de 66 %, suivi de très près par Random Forest et Naive Bayes, tous deux autour de 60 %. Ces scores sont confirmés à la fois par les rapports de classification et le graphique de comparaison des accuracies. La différence entre les modèles est modérée mais nette, avec SVM en tête.

#### NB

```bash
>>> Naive Bayes best parms: {'alpha': 0.1}
 Naive Bayes (mais mieux)
Accuracy : 0.60
              precision    recall  f1-score   support

         pop       0.65      0.24      0.35        46
         rap       0.83      0.64      0.72        45
         rnb       0.51      0.87      0.64        55

    accuracy                           0.60       146
   macro avg       0.66      0.59      0.57       146
weighted avg       0.65      0.60      0.58       146
```
Naive Bayes obtient une accuracy de 60 %. Il présente de bons résultats sur la classe rap avec un rappel de 0.64 et une précision de 0.83, mais il sous-performe sur la classe pop, avec un rappel très faible de 0.24. La classe rnb est relativement bien reconnue avec un rappel de 0.87, mais une précision plus faible (0.51), ce qui indique une tendance à surclasser en rnb. Le F1-score global (pondéré) est de 0.58, ce qui confirme une performance correcte mais limitée.

#### SVM

```bash
>>> SVM best parms: {'C': 1, 'kernel': 'linear'}
 SVM (mais mieux)
Accuracy : 0.66
              precision    recall  f1-score   support

         pop       0.58      0.54      0.56        46
         rap       0.91      0.71      0.80        45
         rnb       0.59      0.73      0.65        55

    accuracy                           0.66       146
   macro avg       0.69      0.66      0.67       146
weighted avg       0.69      0.66      0.67       146
```
SVM atteint une accuracy de 66 %. Il améliore nettement la classification du genre pop par rapport à Naive Bayes, avec un rappel de 0.54 et une précision de 0.58. La classe rap est bien reconnue, avec un rappel élevé de 0.71 et une précision de 0.91, ce qui en fait la classe la mieux maîtrisée par ce modèle. Le genre rnb obtient également de bons résultats, avec un rappel de 0.73 et une précision de 0.59. Le F1-score moyen pondéré atteint 0.67.

#### Random Forest

```bash
>>> Random Forest best parms: {'max_depth': 10, 'min_samples_split': 2, 'n_estimators': 200}
 Random Forest (mais mieux)
Accuracy : 0.60
              precision    recall  f1-score   support

         pop       0.60      0.07      0.12        46
         rap       0.85      0.76      0.80        45
         rnb       0.50      0.93      0.65        55

    accuracy                           0.60       146
   macro avg       0.65      0.58      0.52       146
weighted avg       0.64      0.60      0.53       146
```
Random Forest atteint lui aussi une accuracy de 60 %, mais avec une répartition des performances très déséquilibrée. La classe rap est très bien reconnue avec un rappel de 0.76 et une précision de 0.85. La classe rnb est également bien identifiée avec un rappel de 0.93, mais une précision plus faible de 0.50, ce qui traduit une surclassification vers cette classe. En revanche, la classe pop est presque ignorée, avec un rappel de 0.07 malgré une précision artificiellement élevée de 0.60. Cela indique que le modèle ne reconnaît presque jamais correctement les exemples pop, ce qui dégrade fortement la performance globale et empêche une classification équilibrée. Le F1-score pondéré est de 0.53, inférieur aux deux autres modèles.

### Résultats: Interprétation des performances des modèles évalués sur plusieurs splits aléatoires

Le graphique montre les accuracies moyennes obtenues par les trois modèles sur dix exécutions différentes du pipeline de classification, avec un découpage aléatoire des données à chaque fois. Les barres verticales indiquent l’écart-type des performances, c’est-à-dire la variabilité d’un run à l’autre. Ce type de graphique permet d’évaluer à la fois la performance moyenne et la stabilité des modèles.

SVM est le modèle avec la meilleure accuracy moyenne, aux alentours de 0.64. Il est également relativement stable, avec une variation modérée entre les runs. Naive Bayes et Random Forest atteignent tous deux une accuracy moyenne proche de 0.61. L’écart-type de Naive Bayes est légèrement supérieur à celui de Random Forest, ce qui signifie qu’il est un peu plus sensible à la répartition aléatoire des données. Random Forest est le modèle le plus stable, avec la barre d’erreur la plus courte, bien que son score moyen soit légèrement inférieur à celui du SVM.

Ces résultats confirment que SVM est globalement le modèle le plus performant sur cette tâche. Il conserve une bonne précision même lorsqu’on change le découpage des données, ce qui indique une bonne capacité de généralisation. En revanche, bien que Random Forest soit très stable, sa performance plafonne à un niveau similaire à celui de Naive Bayes, ce qui limite son intérêt dans ce contexte.


