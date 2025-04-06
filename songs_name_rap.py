{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "e44f9aa1-c6b9-451b-b6cc-9a4c7e4dcd7e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Searching for songs by Drake...\n",
      "\n",
      "Song 1: \"God’s Plan\"\n",
      "Song 2: \"In My Feelings\"\n",
      "Song 3: \"Hotline Bling\"\n",
      "Song 4: \"One Dance\"\n",
      "Song 5: \"Hold On, We’re Going Home\"\n",
      "\n",
      "Reached user-specified song limit (5).\n",
      "Done. Found 5 songs.\n",
      "[('God’s Plan', 'Drake'), ('In My Feelings', 'Drake'), ('Hotline Bling', 'Drake'), ('One Dance', 'Drake'), ('Hold On, We’re Going Home', 'Drake')]\n"
     ]
    }
   ],
   "source": [
    "import lyricsgenius\n",
    "\n",
    "# Connection to Genius\n",
    "genius = lyricsgenius.Genius(\"50jzF8g9e2q1IYIel5eR3TT0QLn1p7piS7N0Xv4fzUhpaJuNGUDE5vvnrRJA2nxg\", timeout=15, retries=3, sleep_time=1)\n",
    "genius.skip_non_songs = True\n",
    "genius.excluded_terms = [\"(Remix)\", \"(Live)\"]\n",
    "genius.remove_section_headers = True\n",
    "\n",
    "# US rap artists names \n",
    "rap_artists = [\n",
    "    \"Drake\", \"Kendrick Lamar\", \"J. Cole\", \"Travis Scott\", \"Lil Wayne\",\n",
    "    \"Nicki Minaj\", \"Future\", \"Jay-Z\", \"Nas\", \"Lil Baby\", \"21 Savage\",\n",
    "    \"Doja Cat\", \"Tyler, The Creator\", \"Snoop Dogg\", \"Megan Thee Stallion\",\n",
    "    \"Eminem\", \"Mac Miller\", \"Doechii\", \"Common\"\n",
    "]\n",
    "\n",
    "# Creating songs's list\n",
    "rap_songs = []\n",
    "\n",
    "# Search songs\n",
    "def search_songs_name ():\n",
    "    for artist in rap_artists:\n",
    "        try:\n",
    "            artist_obj = genius.search_artist(artist, max_songs=5, sort=\"popularity\")\n",
    "            for song in artist_obj.songs:\n",
    "                rap_songs.append((f\"{song.title}\", f\"{artist}\"))\n",
    "                if len(rap_songs) >= 100:\n",
    "                    break\n",
    "        except Exception as e:\n",
    "            print(f\"Error with {artist} : {e}\")\n",
    "        if len(rap_songs) >= 100:\n",
    "            break\n",
    "    return\n",
    "\n",
    "search_songs()\n",
    "print(rap_songs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b62a1059-91ba-41c9-9145-e91678e5a2e5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
