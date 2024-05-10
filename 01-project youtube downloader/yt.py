# import youtube_dl
# url = input("Enter url:  \n")
# with youtube_dl.YoutubeDL() as ydl:
#     ydl.download([url])


from pytube import YouTube
link = YouTube("https://www.youtube.com/watch?v=e8cMx3D6MDI")

video = link.streams.get_highest_resolution()
# video = link.streams.get_lowest_resolution()
video.download()

