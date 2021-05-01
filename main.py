import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Authorize spotipy instance
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

# Search for given artist
artist = input("Name of the artist you want to search for: ")
artist_search = sp.search(artist, type="artist")
print(artist_search)
