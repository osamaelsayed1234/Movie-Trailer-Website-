import fresh_tomatoes
import media


#This section is used to initialize the values in the Movie Class in the Media Module for each movie


AYLA = media.Movie(
    "AYLA",
    " Ayla) is a 2017 Turkish drama film directed by Can Ulkay. It was selected as the Turkish entry for the Best Foreign Language Film at the 90th Academy Awards, but it was not nominated",
    "https://upload.wikimedia.org/wikipedia/en/8/89/Ayla_The_Daughter_of_War.jpg",
    "https://www.youtube.com/watch?v=92lnsqRgpFY")

The_Titan   = media.Movie(
    "The Titan",
    "The Titan is a science fiction thriller film directed by Lennart Ruff. It stars Sam Worthington, Taylor Schilling and Tom Wilkinson. The film was released for some countries by Netflix on March 30, 2018",
    "https://upload.wikimedia.org/wikipedia/en/d/dd/The_Titan_poster.png",
    " https://www.youtube.com/watch?v=kQ3fdg7N-2g ")

i_am_a_legend = media.Movie(
    "I am a legend",
    "a story of a man live on his own between zombies",
    "https://goo.gl/7l4m8W",
    "https://www.youtube.com/watch?v=HW8l2Yj1ZK8")

BAD_SAMARITAN = media.Movie("BAD SAMARITAN",
                        "Bad Samaritan is a 2018 American horror-thriller film directed by Dean Devlin and written by Brandon Boyce. The film stars David Tennant and Robert Sheehan, with Carlito Olivero, Kerry Condon, and Jacqueline Byers in supporting roles. Sheehan portrays a valet who burglarizes the houses of the drivers he services, only to discover one of his rich customers (Tennant) is a kidnapper and torturer. It was released in the United States on May 4, 2018",
                        " https://upload.wikimedia.org/wikipedia/en/0/01/BadSamaritanFilm.jpeg ",
                        "https://www.youtube.com/watch?v=yyuRdsik_P0")


matrix = media.Movie("Matrix",
                     "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                     "https://www.movieposter.com/posters/archive/main/9/A70-4902",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

RAMPAGE = media.Movie("RAMPAGE",
                     "Rampage is a 2018 American science fiction monster film directed by Brad Peyton, and loosely based on the video game series of the same name by Midway Games. The film stars Dwayne Johnson, Naomie Harris, Malin Akerman, Jake Lacy, Joe Manganiello, and Jeffrey Dean Morgan. It follows a primatologist named Davis Okoye, who must team up with George, a albino gorilla who turns into a confused but raging creature of enormous size as a result of a rogue experiment. This has to happen in order to stop the two other giant monsters (who were also morphed by the toxic genetic engineering fluid), David Okoye has to retrieve the antidote from Energyne as give it to George. It is the third collaboration between Peyton and Johnson, following Journey 2: The Mysterious Island (2012) and San Andreas (2015) .",
                      "https://upload.wikimedia.org/wikipedia/en/6/6b/Rampage_teaser_film_poster.jpg ",
                     "https://www.youtube.com/watch?v=coOKvrsmQiI ")

mad_max_fury_road = media.Movie("Mad Max Fury Road",
                                "In a stark desert landscape where humanity is broken, two rebels just might be able to restore order: Max, a man of action and of few words, and Furiosa, a woman of action who is looking to make it back to her childhood homeland.",
                                "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSY9szIPbtk1-hwxdEVRJIHT_pgYGNnFkFSWsCjlKFGP3Pu77Oo",
                                "https://www.youtube.com/watch?v=YWNWi-ZWL3c")


whiplash = media.Movie("Whiplash",
                           "A promising young drummer enrolls at a cut-throat music conservatory where his dreams of greatness are mentored by an instructor who will stop at nothing to realize a student's potential.",
                           "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSyLORvKKvCi7-vy8vwi2s8F62aG7D36H15A8rOVfP2d7koyA9I",
                           "https://www.youtube.com/watch?v=tYkuvB2f5XU")

# create a list of all movies in the database of a website

movies = [ AYLA,The_Titan ,i_am_a_legend,BAD_SAMARITAN,  matrix,RAMPAGE, mad_max_fury_road, whiplash]
fresh_tomatoes.open_movies_page(movies)

#"import fresh_tomatoes" allows to turn this code into a movie website by using function "open_movies_page"  
#The "open_movies_page" function takes a list or array of movies, then outputs or creates and opens
#an html webpage or website that shows those movies


