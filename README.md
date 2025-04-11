# Projet Fouille de Texte
Projet de classification automatique des chansons par genre musical selon leurs paroles

---
### Objectif 🎯

Ce projet vise à prédire le genre musical (pop, rap, hip-hop) d'une chanson en analysant uniquement ses paroles (son contenu lexical)

---
### Données 

- Dataset : 
- Genres :
- ~300 chansons au total

---

### Méthodologie

**Prétraitement** des données :
   - Nettoyage des textes (minuscule, ponctuation, etc.)
   - Tokenisation
   - Vectorisation avec Bag-of-Words ou TF-IDF potentiellement
  
**Classification** :
   - Algorithmes possibles :
     - Naive Bayes
     - J48 (arbre de décision)
     - SVM (SMO dans Weka)
   - Évaluation par validation croisée et matrice de confusion 

**Outils**
- Python (pandas, scikit-learn)
- Weka pour la classification (format `.arff`)
- Hugging Face `datasets` potentiellement

