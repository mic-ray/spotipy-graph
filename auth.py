from spotipy.oauth2 import SpotifyClientCredentials
import os

# Authorize using Client Credentials Auth flow
client_id = os.environ.get("spo_client_id")
client_secret = os.environ.get("spo_client_secret")
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
