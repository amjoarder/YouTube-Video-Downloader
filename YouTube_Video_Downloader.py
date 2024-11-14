from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

#print("Title: ",yt.title)
#print("View: ", yt.views)


#Downlaod
yd = yt.streams.get_highest_resolution()
#Put the video link
yd.download('https://www.youtube.com/watch?v=JjpGvjy0Gxk')

'''
run with
python YouTube_Video_Downloader.py https://www.youtube.com/watch?v=JjpGvjy0Gxk
'''