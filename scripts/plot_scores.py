import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les résultats
df = pd.read_csv("resultats_gridsearch.csv")

# Convertir la colonne Accuracy en float (au cas où elle est lue comme string)
df["Accuracy"] = df["Accuracy"].astype(float)

# Afficher les paramètres optimaux (facultatif)
print("Paramètres optimaux par modèle :")
for i, row in df.iterrows():
    print(f"{row['Modèle']} → {row['Meilleurs paramètres']}")

# Plot
plt.figure(figsize=(8, 5))
sns.barplot(x="Modèle", y="Accuracy", data=df, palette="Set2")
plt.ylim(0, 1)
plt.title("Comparaison des performances par modèle")
plt.ylabel("Accuracy")
plt.xlabel("Modèle")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
