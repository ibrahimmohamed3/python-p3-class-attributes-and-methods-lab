class Song:
    count = 0
    genres = []
    artists = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()


    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment
    
     def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    
        def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)
