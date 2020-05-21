from yandex_music.client import Client

class YandexMusicParser:
    def __init__(self, login: str, password: str):
        self.client = Client.from_credentials(login, password)

    def parse_tracks(self) -> list:
        likes_tracks = self.client.users_likes_tracks()
        tracks = []
        track_number = 1

        while True:
            try:
                track = likes_tracks[track_number].track
                title = track.title
                artist = track.artists[0]['name']
                fullname = title + " " + artist
                tracks.append(fullname)
            except IndexError:
                break
            track_number += 1

        return tracks
