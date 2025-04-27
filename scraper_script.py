import lyricsgenius
import os

# Setup Genius API
genius = lyricsgenius.Genius(
    "V8XGT5q8452LoLuZUbQ8zoHekEMxezXCh8dZsG415bBrMPha9_xD-xYAeANHv_9S", 
    timeout=15, retries=3, sleep_time=1
)
genius.skip_non_songs = True
genius.excluded_terms = ["(Remix)", "(Live)"]

#define genre and a sample list of R&B songs
genre = "rnb"  #folder name
songs = [
    ("Pick Up Your Feelings", "Jazmine Sullivan"),
    ("ICU", "Coco Jones"),
    ("When I'm In Your Arms", "Cleo Sol"),
    ("While We're Young", "Jhené Aiko"),
    ("Blue Lights", "Jorja Smith"),
    ("DO 4 LOVE", "Snoh Aalegra"),
    ("Do It", "Chloe x Halle"),
    ("Let It Burn", "Jazmine Sullivan"),
    ("Collide", "Tiana Major9 ft. EARTHGANG"),
    ("Distance", "Yebba"),
    ("Frontin", "Pharrell Williams feat Jay-Z"),
    ("Say So", "PJ Morton ft. JoJo"),
    ("He Wasn't Man Enough", "Toni Braxton"),
    ("Snooze", "SZA"),
    ("You Rock My World", "Michael Jackson"),
    ("John Redcorn", "SiR"),
    ("U Don't Have to Call", "Usher"),
    ("I Wish", "Carl Thomas"),
    ("Love", "Musiq Soulchild"),
    ("Be Here", "Raphael Saadiq feat. D'Angelo"),
    ("A Long Walk", "Jill Scott")
]


#folder store lyrics
output_dir = f"corpus/{genre}"
os.makedirs(output_dir, exist_ok=True)

# Fetch lyrics and save to text files
for idx, (title, artist) in enumerate(songs):
    try:
        song = genius.search_song(title, artist)
        if song and song.lyrics:
            filename = f"{artist.replace(' ', '_')}_{title.replace(' ', '_')}_{idx}.txt".replace("/", "-")
            file_path = os.path.join(output_dir, filename)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(song.lyrics)
            print(f"Saved: {file_path}")
        else:
            print(f"lyrics not found: {title} by {artist}")
    except Exception as e:
        print(f"Error fetching {title} by {artist}: {e}")
