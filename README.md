# Projet Fouille de Texte
Projet de classification des chansons par genre selon leurs paroles

---
### Objectif 🎯

Ce projet vise à prédire le **genre musical** (pop, rap, hip-hop) d'une chanson en analysant uniquement ses **paroles**. L'objectif est d'explorer des approches de fouille de textes pour extraire des caractéristiques linguistiques et émotionnelles pertinentes permettant de différencier les genres musicaux.

---
### Données 

- Dataset : 
- Genres :
- ~300 chansons au total

---

### Méthodologie

**Prétraitement** des données :
   - Nettoyage des paroles
   - Tokenisation
   - Vectorisation via Bag-of-Words et TF-IDF potentiellement
  
**Classification** :
   - Algorithmes possibles :
     - Naive Bayes
     - J48 (arbre de décision)
     - SVM (SMO dans Weka)
   - Évaluation par validation croisée et matrice de confusion 

**Outils**
- Python (pandas, scikit-learn)
- Weka (.arff)
- Hugging Face `datasets` potentiellement

