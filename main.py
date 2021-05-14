from fetch import fetch_album_info
from graph import plot_bar

artist = input("Name of the artist you want to search for: ")


album_info = fetch_album_info(artist)


def calc_avg_length(album_tracks):
    avg = 0
    for track in album_tracks:
        avg += track["duration"]
    return avg//len(album_tracks)


for index, album in enumerate(album_info):
    album_info[index]["avg_track_length"] = calc_avg_length(album["tracks"])

plot_bar([album["name"] for album in album_info], [album["avg_track_length"]
         for album in album_info], "AVG track length in ms")
