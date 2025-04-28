import lyricsgenius 
import time
import os

# Connection to Genius
genius = lyricsgenius.Genius("50jzF8g9e2q1IYIel5eR3TT0QLn1p7piS7N0Xv4fzUhpaJuNGUDE5vvnrRJA2nxg", timeout=15, retries=3, sleep_time=1)
genius.skip_non_songs = True
genius.excluded_terms = ["(Remix)", "(Live)"]
genius.remove_section_headers = True

# US rap artists names 
rap_artists = [
    "Drake", "Kendrick Lamar", "J. Cole", "Travis Scott", "Lil Wayne",
    "Nicki Minaj", "Future", "Jay-Z", "Nas", "Lil Baby", "21 Savage",
    "Doja Cat", "Tyler, The Creator", "Snoop Dogg", "Megan Thee Stallion",
    "Eminem", "Mac Miller", "Doechii", "Common"
]

# Creation of the list
rap_songs = []

# Search songs
def search_songs_name ():
    for artist in rap_artists:
        try:
            artist_obj = genius.search_artist(artist, max_songs=5, sort="popularity")
            for song in artist_obj.songs:
                rap_songs.append((f"{song.title}", f"{artist}"))
                if len(rap_songs) >= 100:
                    break
        except Exception as e:
            print(f"Error with {artist} : {e}")
        if len(rap_songs) >= 100:
            break
    return

search_songs_name()

# Create a directory to store lyrics files
output_dir = "corpus_rap"
os.makedirs(output_dir, exist_ok=True)

# Fetch lyrics and save to text files
for title, artist in rap_songs:
    song = genius.search_song(title, artist)
    if song:
        # Save lyrics to a text file
        file_path = os.path.join(output_dir, f"{artist.replace(' ', '_')}_{title.replace(' ', '_').replace('/', '_').replace('...', '')}.txt")
        with open(file_path, "w", encoding="utf-8") as file:                
            file.write(song.lyrics)
        print(f"Lyrics saved to {file_path}")
    else:
        print(f"Lyrics for '{title}' by {artist} not found.")
