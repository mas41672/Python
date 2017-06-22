class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])
					
bulls_on_parade = Song(["They rally around the family",
						"with pockets full of shells"])
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

strLoveOfMyLife = ["Love of my life",
					"You've hurt me",
					"You've broken my heart",
					"And now you leave me",
					"Love of my life can't you see",
					"bring it back - bring it back",
					"Don't take it away",
					"Cause you don't know",
					"What it means to me"]
print "\n"

loveOfmyLife = Song(strLoveOfMyLife)

loveOfmyLife.sing_me_a_song()