import pafy

print("Enter url:")
url = input()
video = pafy.new(url)

available = video.streams

for i in available:
    print(i)

vid = video.getbest()
print(vid.resolution, vid.extension)

vid.download()
print("DOWNLOAD IS SUCESSFULL")