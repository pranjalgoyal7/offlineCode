from pytube import Playlist

link = 'https://www.youtube.com/playlist?list=PLa6DgTttATAfR8A4kcS2Z0tK83b7caZpt'

yt_playlist = Playlist(link)

yt_playlist.videos

for video in yt_playlist.videos:
    video.streams.get_highest_resolution().download('D:\Devolopment\Projects\Playlist downloader\Filmora_Tutorial')
    print("video downloaded: " + video.title)


print("\n all videos are downloaded from " +yt_playlist.title )