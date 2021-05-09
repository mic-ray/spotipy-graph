import spotipy
from auth import auth_manager
import time

# Create authorized Spotipy instance
sp = spotipy.Spotify(auth_manager=auth_manager)


def convert_to_mins(milliseconds):
    return time.strftime("%M:%S", time.gmtime(
        milliseconds//1000))


def fetch_artist(artist):
    # Search ID of given artist
    artist_search = sp.search(artist, type="artist")
    # Note that the ID of the first artist in the search results is used
    artist_id = artist_search["artists"]["items"][0]["id"]
    return artist_id


def fetch_track_info(artist):
    # Fetch relevant info from the artists albums
    artist_albums = sp.artist_albums(
        artist_id=fetch_artist(artist), album_type="album")

    album_info = [
        {"name": album['name'], "id":album['id'], "date":album['release_date']} for album in artist_albums["items"]]

    album_ids = [album["id"] for album in album_info]

    # Fetch relevant track info of a single album
    track_info = [{"name": track['name'], "id": track['id'], "duration":convert_to_mins(track["duration_ms"])}
                  for track in sp.album_tracks(album_ids[0])["items"]]

    return track_info
