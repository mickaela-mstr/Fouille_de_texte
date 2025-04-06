{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b6e4c57e-38e8-4da7-adb4-04e5d54a1779",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Searching for \"Rich Flex\" by Drake & 21 Savage...\n",
      "Done.\n",
      "Lyrics saved to rap_song_lyrics/Rich_Flex.txt\n",
      "Searching for \"MELTDOWN\" by Travis Scott ft. Drake...\n",
      "Done.\n",
      "Lyrics saved to rap_song_lyrics/MELTDOWN.txt\n",
      "Searching for \"FE!N\" by Travis Scott ft. Playboi Carti...\n",
      "Done.\n",
      "Lyrics saved to rap_song_lyrics/FE!N.txt\n",
      "Searching for \"Search & Rescue\" by Drake...\n",
      "Done.\n",
      "Lyrics saved to rap_song_lyrics/Search_&_Rescue.txt\n",
      "Searching for \"IDGAF\" by Drake ft. Yeat...\n",
      "Done.\n",
      "Lyrics saved to rap_song_lyrics/IDGAF.txt\n"
     ]
    }
   ],
   "source": [
    "import lyricsgenius \n",
    "import time\n",
    "import os\n",
    "\n",
    "genius = lyricsgenius.Genius(\"50jzF8g9e2q1IYIel5eR3TT0QLn1p7piS7N0Xv4fzUhpaJuNGUDE5vvnrRJA2nxg\", timeout=15, retries=3, sleep_time=1)\n",
    "\n",
    "rap_songs = [\n",
    "    (\"Rich Flex\", \"Drake & 21 Savage\"),\n",
    "    (\"MELTDOWN\", \"Travis Scott ft. Drake\"),\n",
    "    (\"FE!N\", \"Travis Scott ft. Playboi Carti\"),\n",
    "    (\"Search & Rescue\", \"Drake\"),\n",
    "    (\"IDGAF\", \"Drake ft. Yeat\")\n",
    "]\n",
    "\n",
    "# Create a directory to store lyrics files\n",
    "output_dir = \"rap_songs_lyrics\"\n",
    "os.makedirs(output_dir, exist_ok=True)\n",
    "\n",
    "# Fetch lyrics and save to text files\n",
    "for title, artist in rap_songs:\n",
    "    song = genius.search_song(title, artist)\n",
    "    if song:\n",
    "        # Save lyrics to a text file\n",
    "        file_path = os.path.join(output_dir, f\"{title.replace(' ', '_')}.txt\")\n",
    "        with open(file_path, \"w\", encoding=\"utf-8\") as file:                \n",
    "            file.write(song.lyrics)\n",
    "        print(f\"Lyrics saved to {file_path}\")\n",
    "    else:\n",
    "        print(f\"Lyrics for '{title}' by {artist} not found.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53b61ed8-8537-4404-a9e0-2a4addec884c",
   "metadata": {},
   "outputs": [],
   "source": [
    "pip install lyricsgenius"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "13a905dd-95ca-40db-abe8-6ed299e3d8d7",
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
