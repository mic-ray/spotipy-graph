from fetch import fetch_album_info
from graph import plot_bar


def calculate_avg_artist_tracks_length(artist):
    album_info = fetch_album_info(artist)
    for index, album in enumerate(album_info):
        album_info[index]["avg_track_length"] = calculate_avg_album_length(
            album["tracks"]
        )
        print(calculate_avg_album_length(album["tracks"]))
    return album_info


def calculate_avg_track_length(album_tracks):
    avg = 0
    for track in album_tracks:
        avg += track["duration"]
    return avg // len(album_tracks)


def plot_album(album_info):
    plot_bar(
        [album["name"] for album in album_info],
        [album["avg_track_length"] for album in album_info],
        "AVG track length in ms",
    )


def main():
    artist = input("Name of the artist you want to search for: ")
    album_info = calculate_avg_artist_tracks_length(artist)
    plot_album(album_info)


if __name__ == "__main__":
    main()
