import lyricsgenius 
import time
import os

genius = lyricsgenius.Genius("50jzF8g9e2q1IYIel5eR3TT0QLn1p7piS7N0Xv4fzUhpaJuNGUDE5vvnrRJA2nxg", timeout=15, retries=3, sleep_time=1)

rap_songs = [
    ("Rich Flex", "Drake & 21 Savage"),
    ("MELTDOWN", "Travis Scott ft. Drake"),
    ("FE!N", "Travis Scott ft. Playboi Carti"),
    ("Search & Rescue", "Drake"),
    ("IDGAF", "Drake ft. Yeat")
]

# Create a directory to store lyrics files
output_dir = "rap_songs_lyrics"
os.makedirs(output_dir, exist_ok=True)

# Fetch lyrics and save to text files
for title, artist in rap_songs:
    song = genius.search_song(title, artist)
    if song:
        # Save lyrics to a text file
        file_path = os.path.join(output_dir, f"{artist.replace(' ', '_')}_{title.replace(' ', '_')}.txt")
        with open(file_path, "w", encoding="utf-8") as file:                
            file.write(song.lyrics)
        print(f"Lyrics saved to {file_path}")
    else:
        print(f"Lyrics for '{title}' by {artist} not found.")
