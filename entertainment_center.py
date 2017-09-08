from media import Movie
import fresh_tomatoes

# creating array and Movie objects
movie_list = [
    Movie(
        movie_title="Avatar",
        movie_trailer="https://www.youtube.com/watch?v=cRdxXPV9GNQ",
        movie_poster="https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
        movie_storyline="The film is set in the mid-22nd century, when humans are colonizing Pandora, a lush "
                        "habitable moon of a gas giant in the Alpha Centauri star system, in order to mine the mineral "
                        "unobtanium, a room-temperature superconductor. The expansion of the mining colony "
                        "threatens the continued existence of a local tribe of Na'vi – a humanoid species indigenous "
                        "to Pandora."),
    Movie(
        movie_title="Avengers",
        movie_trailer="https://www.youtube.com/watch?v=eOrNdBpGMv8",
        movie_poster="https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",
        movie_storyline=""),
    Movie(
        movie_title="Big Hero 6",
        movie_trailer="https://www.youtube.com/watch?v=rD5OA6sQ97M",
        movie_poster="https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",
        movie_storyline=""),
    Movie(
        movie_title="Final Fantasy: The Spirits Within",
        movie_trailer="https://www.youtube.com/watch?v=GnE64DbnUzY",
        movie_poster="https://upload.wikimedia.org/wikipedia/en/3/34/Final_Fantasy_The_Spirits_Within_%282011_film%29_poster.jpg",
        movie_storyline=""),
    Movie(
        movie_title="Hitchikers Guide to the Galaxy",
        movie_trailer="https://www.youtube.com/watch?v=MbGNcoB2Y4I",
        movie_poster="https://upload.wikimedia.org/wikipedia/en/7/7a/Hitchhikers_guide_to_the_galaxy.jpg",
        movie_storyline=""),
    Movie(
        movie_title="Iron Man",
        movie_trailer="https://www.youtube.com/watch?v=8hYlB38asDY",
        movie_poster="https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
        movie_storyline="")
]

# command to build the movie page based on list created above
if __name__ == '__main__':
    fresh_tomatoes.open_movies_page(movie_list)
