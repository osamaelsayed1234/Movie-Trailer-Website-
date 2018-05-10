import webbrowser  # this import the webbrowser package from the main packages


class Movie(object):
    """ This class will be used to create instances of a movie, which will be used to populate
    the fresh tomatoes website """

    # constructor
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):

        # instance variables
        self.title = movie_title  #This is the title of the movie  
        self.storyline = movie_storyline  # movie description
        self.poster_image_url = poster_image  # This is the image url for the movie poster
        self.trailer_youtube_url = trailer_youtube  #This is a url to the movie trailer on youtube.


    #instance method
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
