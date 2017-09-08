import webbrowser


# Parent class to TvShow and Movie
class Video:
    def __init__(self, title, duration):
        # initializing parent variables
        self.title = title
        self.duration = duration


class TvShow(Video):
    def __init__(self, show_title=None, show_duration=None, show_season=None, show_episode=None, show_station=None):
        # calling parent initialization
        Video.__init__(self, title=show_title, duration=show_duration)
        # setting TvShow instance variables
        self.season = show_season
        self.episode = show_episode
        self.station = show_station


class Movie(Video):
    def __init__(self, movie_title=None, movie_trailer=None, movie_poster=None, movie_storyline=None,
                 movie_duration=None):
        """
        Initializing variables for an instance of Movie

        :param movie_title: title of the movie
        :type movie_title: str

        :param movie_trailer: url for the trailer
        :type movie_trailer: str

        :param movie_poster: url for the poster
        :type movie_poster: str

        :param movie_storyline: synopsis of the movie
        :type movie_storyline: str
        """
        # calling parent initialization
        Video.__init__(self, title=movie_title, duration=movie_duration)
        # setting Movie instance variables
        self.trailer_youtube_url = movie_trailer
        self.poster_image_url = movie_poster
        self.storyline = movie_storyline

    def show_trailer(self):
        """
        opens a web page to the url stored in trailer_youtube_url
        :return: None
        """
        # Checking to make sure the variable is not None (as it is not mandatory when creating Movie instance)
        if self.trailer_youtube_url:
            webbrowser.open(self.trailer_youtube_url, 1)
        # print error message if there is nothing in the variable
        else:
            print("Error - trailer variable not set.")
