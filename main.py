import spotipy
from auth import auth_manager

import time


def convert_to_mins(milliseconds):
    return time.strftime("%M:%S", time.gmtime(
        milliseconds//1000))


# Create authorized Spotipy instance
sp = spotipy.Spotify(auth_manager=auth_manager)

# Search ID of given artist
artist = input("Name of the artist you want to search for: ")
artist_search = sp.search(artist, type="artist")

# Note that the ID of the first artist in the search results is used
artist_id = artist_search["artists"]["items"][0]["id"]

# Fetch relevant info from the artists albums
artist_albums = sp.artist_albums(
    artist_id=artist_id, album_type="album")
album_info = [
    {"name": album['name'], "id":album['id'], "date":album['release_date']} for album in artist_albums["items"]]

# Fetch relevant track info of a single album
album_ids = [x["id"] for x in album_info]

track_info = [{"name": track['name'], "id": track['id'], "duration":convert_to_mins(track["duration_ms"])}
              for track in sp.album_tracks(album_ids[0])["items"]]

print(track_info)
