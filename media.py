__author__ = 'joe'

import webbrowser


class Video():
    """ Parent class "Video". Stores information for the title and duration of a video.
    """
    # Initialization for Video class
    def __init__(self, title, duration):
        # Using passed variables to initialize class variables
        self.title = title
        self.duration = duration


class Movie(Video):
    """  This class provides a way to store movie related information, inherited from Video class
    """
    # Unimplemented ratings to verify valid ratings for movies
    VALID_RATINGS = ["G", "PC", "PG-13", "R", "NC-17"]

    # Initialization for Movie class
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_url):
        # Providing information to Video parent
        Video.__init__(self, movie_title, "0:00")
        # Initializing additional variables that are specific to Movie class using passed variables
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url
    # Function in Movie class to open a web browser to the trailer on YouTube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)