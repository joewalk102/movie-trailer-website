import media
import fresh_tomatoes

movies = []
movies.append(media.Movie("Guardians of the Galaxy",
                          "Brash space adventurer Peter Quill (Chris Pratt) finds himself the quarry of relentless bounty hunters after he steals an orb coveted by Ronan, a powerful villain",
                          "http://t2.gstatic.com/images?q=tbn:ANd9GcQW3LbpT94mtUG1PZIIzJNxmFX399wr_NcvoppJ82k7z99Hx6in",
                          "https://www.youtube.com/watch?v=LbHz7SkqXzA"))

movies.append(media.Movie("Avatar",
                          "A marine on an alien planet",
                          "http://cafmp.com/wp-content/uploads/2012/11/French-Avatar-Poster",
                          "https://www.youtube.com/watch?v=5PSNL1qE6VY"))

movies.append(media.Movie("Van Wilder",
                          "The most popular kid on campus meets a beautiful journalist who makes him realize that maybe he's afraid to graduate.",
                          "http://movienewz.nl/img/photos/wilder.jpg",
                          "https://www.youtube.com/watch?v=K19UvDbuD0A"))

movies.append(media.Movie("The Grand Budapest Hotel",
                          "In the 1930s, the Grand Budapest Hotel is a popular European ski resort, presided over by concierge Gustave H. (Ralph Fiennes)..",
                          "http://t0.gstatic.com/images?q=tbn:ANd9GcSDDmHpt0TcHkK9DCv0QU-Xx4WNEVOJnHlj7pVfN61-1mEX2eCG",
                          "https://www.youtube.com/watch?v=dGaeLgtH_8A"))

movies.append(media.Movie("Interstellar",
                          "In Earth's future, a global crop blight and second Dust Bowl are slowly rendering the planet uninhabitable.",
                          "http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB",
                          "https://www.youtube.com/watch?v=0vxOhd4qlnA"))

movies.append(media.Movie("Big Hero 6",
                          "Robotics prodigy Hiro (Ryan Potter) lives in the city of San Fransokyo.",
                          "http://t2.gstatic.com/images?q=tbn:ANd9GcQzyu98HxFhB68UKqRKSrTKknXHI-gtSTAAX0CGiKBM980CFhI1",
                          "https://www.youtube.com/watch?v=Sh5EO5h_do0"))

movies.append(media.Movie("Kingsman: The Secret Service",
                          "Gary 'Eggsy' Unwin (Taron Egerton), whose late father secretly worked for a spy organization, lives in a South London housing estate and seems headed for a life behind bars",
                          "http://t3.gstatic.com/images?q=tbn:ANd9GcTn2E6bqcLehK92h215qFnUpCYFqt02Iuwg-N4gVBmixzAXvGfZ",
                          "https://www.youtube.com/watch?v=t7ybRKVCUxM"))

fresh_tomatoes.open_movies_page(movies)
