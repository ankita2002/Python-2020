import pafy

print("Enter video url:")
link = input()
vid = pafy.new(link)

song = vid.getbestaudio()
song.download()