import fresh_tomatoes
import media
"#list of Movies with all it's information that will be"
"#used to display the data on the website this data include"
"#the movie name , description , photo URL , youtube trailer URL"

The_Titan = media.Movie(
     "The Titan",
     "The Titan is a science fiction thriller film directed by Lennart Ruff",
     "https://upload.wikimedia.org/wikipedia/en/d/dd/The_Titan_poster.png",
     "https://www.youtube.com/watch?v=kQ3fdg7N-2g")

i_am_a_legend = media.Movie(
     "I am a legend",
     "a story of a man live on his own between zombies",
     "https://goo.gl/7l4m8W",
     "https://www.youtube.com/watch?v=HW8l2Yj1ZK8")


intersteller = media.Movie(
     "INTERSTELLER",
     "a story of a pilot travel throw space",
     "https://goo.gl/pDVNBG",
     "https://www.youtube.com/watch?v=zSWdZVtXT7E")

toy_story = media.Movie(
    "Toy story",
    "a story of a boy and his toys that comes to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=JcpWXaA2qeg")
movies = [The_Titan, i_am_a_legend, intersteller, toy_story]

fresh_tomatoes.open_movies_page(movies)

'# create a list of all movies in the database of a website'
'# calling the opening function that is going to display this data'
'# in such a style with all of the information we put in the list variables'
