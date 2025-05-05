import os
import re
import glob
import pandas as pd
from collections import defaultdict

def clean_lyrics(raw_text):
    lines = raw_text.splitlines()
    filtered_lines = []
    start_recording = False

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Démarre à partir du premier bloc de paroles repéré par [Chorus], [Verse], etc.
        if not start_recording and len(re.findall(r"\b\w+\b", line)) >= 1:
            start_recording = True

        if start_recording:
            line = re.sub(r"\[.*?\]", "", line).strip()  # ← enleve les titres entre []
            if line:
                filtered_lines.append(line)

    return "\n".join(filtered_lines)

pop_folder = "corpus/pop/*"
rap_folder = "corpus/rap/*"
rnb_folder = "corpus/rnb/*"
pop_files = glob.glob(pop_folder)
rap_files = glob.glob(rap_folder)
rnb_files = glob.glob(rnb_folder)


dico = {
    "pop" : pop_files,
    "rnb" : rnb_files,
    "rap" : rap_files}

def get_table(dico):
    
    dict_lyrics = defaultdict(list)

    for genre, files in dico.items():
        for file in files:
            with open(file, "r", encoding="utf-8") as f:
                if genre == "rap":
                    lines = f.readlines()
                    raw_lyrics = "".join(lines[1:])  # enlève la première ligne
                else:
                    raw_lyrics = f.read()

            cleaned_lyrics = clean_lyrics(raw_lyrics)
            dict_lyrics["Parole"].append(cleaned_lyrics)
            dict_lyrics["Genre"].append(genre)
            dict_lyrics["Titre + artiste"].append(os.path.basename(file))

    df = pd.DataFrame(dict_lyrics)
    df.to_csv("lyrics.csv", index=False)

get_table(dico)
