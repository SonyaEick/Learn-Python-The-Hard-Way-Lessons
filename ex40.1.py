class Song(object):

   def _init_(self, lyrics):
      self.lyrics = lyrics
   def sing(self):
      for line in self.lyrics:
         print line

bday = Song(["Happy birthday to you",
"I dont want to get sued",
"So I'll stop right there"])

bulls = Song(["They rally around the family",
"With a pocket full of shells"])

bday.sing()

bulls.sing()
