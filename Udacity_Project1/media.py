__author__ = 'joe'

import webbrowser


class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class Movie(Video):
    """  This class provides a way to store movie related information
    """
    VALID_RATINGS = ["G", "PC", "PG-13", "R", "NC-17"]
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_url):
        Video.__init__(self, movie_title, "0:00")
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)