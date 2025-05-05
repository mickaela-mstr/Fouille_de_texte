import lyricsgenius 
import os
import argparse
from tqdm import tqdm

### POUR RÉCUPÉRER À PARTIR DE L'ARTISTE ###
# On utilise le nom du gadjo pour choper ses chansons
def get_artist_songs(artist_name, genius, max_songs):

    try:
        artist = genius.search_artist(artist_name, max_songs=max_songs, sort="popularity", include_features=False)
        if artist:
            return [(song.title, artist.name) for song in artist.songs]
        else:
            print(f"Aucun résultat pour l’artiste : {artist_name}")
        return []
        
    except Exception as e:
        print(f"Erreur lors de la recherche de l'artiste {artist_name} : {e}")
        return []
    

def searchbysongs(songs, genius, genre):

    #  POUR RÉCUPÉRER À PARTIR D'UNE LISTE DE CHANSONS #
    # pop_songs = [
    #     ("Blinding Lights", "The Weeknd"),
    #     ("Shape of You", "Ed Sheeran"),
    #     ("Levitating", "Dua Lipa"),
    #     ("Bad Guy", "Billie Eilish"),
    # ]

    # Récupération des paroles avec gestion des erreurs
    for title, artist in tqdm(songs):
        try:
            song = genius.search_song(title, artist)
            if song:
                savesong(song.lyrics, title, artist, output_dir)
            else:
                print(f"Lyrics for '{title}' by {artist} not found.")

        except Exception as e:
            print(f"Erreur pour '{title}' de {artist} : {e}")


def savesong(lyrics, title, artist, output_dir):
    """
    Sauvegarde les paroles d'une chanson dans un fichier texte.
    """
    
    file_path = os.path.join(output_dir, f"{artist}_{title.replace(' ', '_')}.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(lyrics)
    print(f"Lyrics saved to {file_path}")
        


def main():


    parser = argparse.ArgumentParser(description="Récupérer les paroles de chansons d'un artiste.")
    parser.add_argument("-a", "--artist", type=str, help="Nom de l'artiste dont on veut récupérer les paroles.")
    parser.add_argument("-g", "--genre", type=str, help="Genre de musique (ex: pop, rock, rap).",
                        choices=["pop", "rap", "r&b"])

    args = parser.parse_args()
    # ex artist = "Dua Lipa"

    genius = lyricsgenius.Genius(
        "50jzF8g9e2q1IYIel5eR3TT0QLn1p7piS7N0Xv4fzUhpaJuNGUDE5vvnrRJA2nxg",
        sleep_time=20,
        timeout=15,
        retries=1
    )


    artist = args.artist if args.artist else "Dua Lipa" 
    genre = args.genre if args.genre else "pop"
    print(f"Récupération des paroles de l'artiste : {artist} dans le genre : {genre}...")

    songs = get_artist_songs(artist, genius, max_songs=20)
    searchbysongs(songs, genius, genre)

if __name__ == "__main__":
    main()
 