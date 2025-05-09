import pandas as pd
import matplotlib.pyplot as plt

# Charger les résultats
df = pd.read_csv("perf_modeles.csv")

# Convertir les colonnes en float
df["Accuracy moyenne"] = df["Accuracy moyenne"].astype(float)
df["Écart-type"] = df["Écart-type"].astype(float)

# Tracer le graphe avec barres d'erreur (matplotlib pur)
plt.figure(figsize=(8, 5))
x = df["Modèle"]
y = df["Accuracy moyenne"]
yerr = df["Écart-type"]

plt.bar(x, y, yerr=yerr, capsize=5, color=["#8dd3c7", "#ffffb3", "#bebada"])
plt.title("Perf des modèles sans random state (accuracy ± écart-type)")
plt.ylabel("Accuracy moyenne")
plt.ylim(0, 1)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
