from pytube import YouTube

link = input('Enter YouTube Video link')

yt = YouTube(link)

ytaudiodownload = yt.streams.get_lowest_resolution()

ytaudiodownload.download()

print("video successfully downloaded")