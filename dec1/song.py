class Song(object):
	def __init__(self, lyrics, artist=''):
		self.lyrics = lyrics
		self.artist = artist

	def sing(self):
		print "Artist: " + self.artist

		for line in self.lyrics:
			print line

if __name__ == '__main__':
	foals = Song(["You don't have my number"], "foals")
	foals.sing()

	unaware = Song(["push, pull, tear"])
	unaware.sing()


