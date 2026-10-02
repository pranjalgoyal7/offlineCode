from pytube import YouTube

link = input('Enter YouTube Video link')

yt = YouTube(link)

# for stream in yt.streams:
#     print(stream)

# print(yt.streams.get_by_itag('134'))


# print(yt.streams.filter(progressive='True'))

# ytvideodownload= yt.streams.get_by_itag('134')
# ytvideodownload.download()


print("\nAll streams are printed")