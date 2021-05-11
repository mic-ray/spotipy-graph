from fetch import fetch_album_info
import pprint

artist = input("Name of the artist you want to search for: ")

pprint.pprint(fetch_album_info(artist))
