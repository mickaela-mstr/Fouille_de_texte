import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

"""
nuage de mot pour voir les mots qui revienne le plus par genre

"""

df = pd.read_csv("lyrics.csv")

custom_stopwords = {
    "oh", "yeah", "uh", "uhh", "uhhh", "la", "na", "woo", "ooh", "ah", "ahh", "ayy", "ay", "yo",
    "got", "gonna", "wanna", "im", "ive", "dont", "aint", "ya", "youre", "youve", "thats", "hey",
    "like", "just", "know", "yeah", "ohh", "i", "me", "my", "let", "get", "gotta", "one"
}

def clean_text(text):
    words = text.lower().split()
    words = [word for word in words if word.isalpha() and word not in custom_stopwords]
    return ' '.join(words)

genres = df["Genre"].unique()

for genre in genres:
    text = ' '.join(df[df["Genre"] == genre]["Parole"].dropna().astype(str).tolist())
    text = clean_text(text)
    wc = WordCloud(width=800, height=400, background_color='white', max_words=100).generate(text)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.title(f"Nuage de mots - {genre}")
    plt.tight_layout()
    plt.savefig(f"résultats/wordcloud_{genre}.png")
    plt.close()