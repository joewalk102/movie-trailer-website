import media
import fresh_tomatoes

# Creating an array to put in objects of type "Movie()" which is a child class of "Video"
movies = []

# Creating instances of class Movie in the movies collection array.
movies.append(media.Movie(movie_title="Guardians of the Galaxy",
                          movie_storyline="Brash space adventurer Peter Quill (Chris Pratt) finds himself the quarry "
                                          "of relentless bounty hunters after he steals an orb coveted by Ronan, a "
                                          "powerful villain",
                          poster_image="http://t2.gstatic.com/images?q=tbn:ANd9GcQW3LbpT94mtUG1PZIIzJNxmFX399wr_"
                                       "NcvoppJ82k7z99Hx6in",
                          trailer_url="https://www.youtube.com/watch?v=LbHz7SkqXzA"))

movies.append(media.Movie(movie_title="Avatar",
                          movie_storyline="A marine on an alien planet",
                          poster_image="http://cafmp.com/wp-content/uploads/2012/11/French-Avatar-Poster",
                          trailer_url="https://www.youtube.com/watch?v=5PSNL1qE6VY"))

movies.append(media.Movie(movie_title="Van Wilder",
                          movie_storyline="The most popular kid on campus meets a beautiful journalist who makes him "
                                          "realize that maybe he's afraid to graduate.",
                          poster_image="http://movienewz.nl/img/photos/wilder.jpg",
                          trailer_url="https://www.youtube.com/watch?v=K19UvDbuD0A"))

movies.append(media.Movie(movie_title="The Grand Budapest Hotel",
                          movie_storyline="In the 1930s, the Grand Budapest Hotel is a popular European ski resort, "
                                          "presided over by concierge Gustave H. (Ralph Fiennes)..",
                          poster_image="http://t0.gstatic.com/images?q=tbn:ANd9GcSDDmHpt0TcHkK9DCv0QU-"
                                       "Xx4WNEVOJnHlj7pVfN61-1mEX2eCG",
                          trailer_url="https://www.youtube.com/watch?v=dGaeLgtH_8A"))

movies.append(media.Movie(movie_title="Interstellar",
                          movie_storyline="In Earth's future, a global crop blight and second Dust Bowl are slowly "
                                          "rendering the planet uninhabitable.",
                          poster_image="http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-"
                                       "VogMH8LfZHEaq3UdCMLxARZAB",
                          trailer_url="https://www.youtube.com/watch?v=0vxOhd4qlnA"))

movies.append(media.Movie(movie_title="Big Hero 6",
                          movie_storyline="Robotics prodigy Hiro (Ryan Potter) lives in the city of San Fransokyo.",
                          poster_image="http://t2.gstatic.com/images?q=tbn:ANd9GcQzyu98HxFhB68UKqRKSrTKknXHI-"
                                       "gtSTAAX0CGiKBM980CFhI1",
                          trailer_url="https://www.youtube.com/watch?v=Sh5EO5h_do0"))

movies.append(media.Movie(movie_title="Kingsman: The Secret Service",
                          movie_storyline="Gary 'Eggsy' Unwin (Taron Egerton), whose late father secretly worked for a "
                                          "spy organization, lives in a South London housing estate and seems headed "
                                          "for a life behind bars",
                          poster_image="http://t3.gstatic.com/images?q=tbn:ANd9GcTn2E6bqcLehK92h215qFnUpCYFqt02Iuwg-"
                                       "N4gVBmixzAXvGfZ",
                          trailer_url="https://www.youtube.com/watch?v=t7ybRKVCUxM"))

# Using fresh_tomatoes python file to generate and open a web page using the information stored in movies array
fresh_tomatoes.open_movies_page(movies)
