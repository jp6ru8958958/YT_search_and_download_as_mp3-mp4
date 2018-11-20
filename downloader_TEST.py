import requests
from bs4 import BeautifulSoup
import sys
import youtube_dl
from pytube import YouTube
URL=""
url = "https://www.youtube.com/results?sp=CAM%253D&search_query="+str(input("輸入關鍵字:"))
request = requests.get(url)
content = request.content
soup = BeautifulSoup(content, "html.parser")
user_check='0'
for all_video in soup.select(".yt-lockup-video"):
    if user_check=='0':
        data = all_video.select("a[rel='spf-prefetch']")
        data2 = all_video.select(".yt-lockup-meta-info")
        time = data2[0].get_text("#").split("#")[0]
        see = data2[0].get_text("#").split("#")[1]
        print(data[0].get("title"))
        print(see)        
        user_check=str(input("你要找的是這首歌嗎?是的話請輸入1不是的話請輸入0:"))
    elif user_check=='1':
        URL="https://www.youtube.com{}".format(data[0].get("href"))
        break
       # print(URL,"開始下載")
#==============================================================================
download=input("使用功能")

if download == "mp3" or download == "MP3":
    ydl_opts = {'format': 'bestaudio/best','postprocessors':
        [{
	  'key': 'FFmpegExtractAudio',
	  'preferredcodec': 'mp3',
	  'preferredquality': '320',
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([URL])
    print("下載完成")
    
elif download == "mp4":
    filelocationtxt = open("C:\\Users\\jp6ru\\OneDrive\\桌面\\youtubedownload\\download.txt",'r')
    filelocation = filelocationtxt.read()
    yt = YouTube(URL)
    stream = yt.streams.filter(file_extension='mp4', res=0).first()
    stream.download(filelocation)
    print("下載完成,已下載至"+ filelocation)