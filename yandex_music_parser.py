from yandex_music.client import Client

class YandexMusicParser:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.tracks = []

    def tracks_parse(self):
        client = Client.from_credentials(self.login, self.password)
        likes_tracks = client.users_likes_tracks()
        track_number = 1

        while True:
            try:
                track = likes_tracks[track_number].track
                title = track.title
                artist = track.artists[0]['name']
                fullname = title + " " + artist
                self.tracks.append(fullname)
            except IndexError:
                break
            track_number += 1

        return self.tracks
