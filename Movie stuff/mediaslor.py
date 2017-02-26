import webbrowser

class Movie():

    def __init__ (self, movie_title, movie_storyline, movie_poster,
                  movie_youlink):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster = movie_poster
        self.link = movie_youlink


    def open_trailer(self, title):
        webbrowser.open(title)

        
