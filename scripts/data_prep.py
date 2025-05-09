import os
import re
import glob
import pandas as pd
from collections import defaultdict

def clean_lyrics(raw_text):
    lines = raw_text.splitlines()
    non_empty_lines = [line.strip() for line in lines if line.strip()]

    # Cas 1 : le texte contient des balises [Chorus], [Verse], etc.
    has_tags = any(re.match(r"\[.*?\]", line) for line in non_empty_lines)

    filtered_lines = []

    if has_tags:
        start_recording = False
        for line in non_empty_lines:
            if not start_recording and re.match(r"\[.*?\]", line):
                start_recording = True
            if start_recording:
                line = re.sub(r"\[.*?\]", "", line).strip()
                if line:
                    filtered_lines.append(line)
    else:
        # Cas 2 : pas de balises → on ignore juste la première ligne
        filtered_lines = non_empty_lines[1:]

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
                raw_lyrics = f.read()
                cleaned_lyrics = clean_lyrics(raw_lyrics)
                dict_lyrics["Parole"].append(cleaned_lyrics)
                dict_lyrics["Genre"].append(genre)
                dict_lyrics["Titre + artiste"].append(os.path.basename(file))

    df = pd.DataFrame(dict_lyrics)
    df.to_csv("lyrics.csv", index=False)

get_table(dico)