
import os
import glob
import pandas as pd
from collections import defaultdict

pop_folder = "pop_song_lyrics"
rap_folder = "rap_song_lyrics"
rnb_folder = "rnb_song_lyrics"
pop_files = glob.glob(os.path.join(pop_folder, "*.txt"))
rap_files = glob.glob(os.path.join(rap_folder, "*.txt"))
rnb_files = glob.glob(os.path.join(rnb_folder, "*.txt"))


dico = {
    "pop" : pop_files,
    "rnb" : rnb_files
}

def get_table(dico):

    
    dict_lyrics = defaultdict(list)

    for genre, files in dico.items():
        for file in files:
            with open(file, "r", encoding="utf-8") as f:
                lyrics = f.read()
                dict_lyrics["Text"].append(lyrics)
                dict_lyrics["Genre"].append(genre)

    df = pd.DataFrame(dict_lyrics)
    df.to_csv("lyrics.csv", index=False)
    

get_table(dico)
