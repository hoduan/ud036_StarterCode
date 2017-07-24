import webbrowser

class Movie():
	'''This class defines a movie prototype'''

	def __init__(self, movie_title, movie_storyline, movie_poster_img, movie_youtube_url):
			self.title = movie_title
			self.movie_storyline = movie_storyline
			self.poster_image_url = movie_poster_img
			self.trailer_youtube_url = movie_youtube_url


	def paly_trailer(self):
			webbrowser.open(self.trailer_youtube_url)
