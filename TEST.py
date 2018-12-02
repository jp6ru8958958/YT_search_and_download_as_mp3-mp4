<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup
import sys
import youtube_dl
from pytube import YouTube

URL = ""
url = "https://www.youtube.com/results?sp=CAM%253D&search_query=" + str(input("輸入關鍵字:"))
request = requests.get(url)
content = request.content
soup = BeautifulSoup(content, "html.parser")
user_check = '0'
for all_video in soup.select(".yt-lockup-video"):
    if user_check == '0':
        video_name = all_video.select("a[rel='spf-prefetch']")
        video_watchtimes = all_video.select(".yt-lockup-meta-info")
#        time = video_watchtime[0].get_text("#").split("#")[0]
        see = video_watchtimes[0].get_text("#").split("#")[1]

        print(video_name[0].get("title"))
        print(see)
        user_check = str(input("你要找的是這首歌嗎?是的話請輸入1不是的話請輸入0:"))
    elif user_check == '1':
        URL = "https://www.youtube.com{}".format(video_name[0].get("href"))
        break
    # print(URL,"開始下載")
# ==============================================================================
download = input("使用功能")

if download == "mp3" or download == "MP3":
    ydl_opts = {'format': 'bestaudio', 'postprocessors':
        [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }]
                }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([URL])
    print("下載完成")

elif download == "mp4" or download == "MP4":
    with youtube_dl.YoutubeDL({'format': 'bestaudio'}) as ydl:
        ydl.download([URL])
    print("下載完成")
=======
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


student = Student("ok", 100)
print(student.name, student.score)
>>>>>>> b4fd5fcbe62d9c0c62386b832ae88f1fa6f58f77
