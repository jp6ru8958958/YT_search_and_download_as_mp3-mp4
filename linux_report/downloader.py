import requests                         # 用來取得網頁原始碼
from bs4 import BeautifulSoup           # 用來對取得的網頁原始碼做解析,找出需要的內容
import youtube_dl                       # 下載器
# 函式庫皆從github上找到官方使用說明
#https://www.youtube.com/results?sp=CAM%253D&search_query=%E6%A0%B9%E6%9C%AC%E5%B0%B1

URL = ""
url = "https://www.youtube.com/results?sp=CAM%253D&search_query=" + str(input("輸入關鍵字:")) # youtube的搜尋規則為(搜尋方式)+(關鍵字),這裡使用依觀看次數來搜尋的方式
request = requests.get(url)             # 取得目標網頁的原始碼
content = request.content

soup = BeautifulSoup(content, "html.parser")
user_check = '0'

for all_video in soup.select(".yt-lockup-video"):   #爬蟲區請搭配網頁原始碼服用

    if user_check == '0':
        video_name = all_video.select("a[rel='spf-prefetch']")          # rel="spf-prefetch"用來選取a標籤下的東西
        video_watchtimes = all_video.select(".yt-lockup-meta-info")     # 取得標題下方資訊的內容

        print(video_name[0].get("title"))                               # 使用get()讀出在"title"的內容
        print("發佈時間"+video_watchtimes[0].get_text(" "))              # 直接印出整個內容,get_text的功能只有在中間增加一個空格做區隔

        user_check = str(input("你要找的是這首歌嗎?是的話請輸入1不是的話請輸入0:"))   #選定影片或查看下一個搜尋結果

    elif user_check == '1':     # 輸入"1"時選定下載的影片,並跳出迴圈前往下載器的部分
        URL = "https://www.youtube.com{}".format(video_name[0].get("href"))     # 影片連結的位置一樣在a標籤下,只是位置為"href"
        break                                                                   # {}為python語法,內容是後面format的內容

# download=========================================================================
# https://github.com/rg3/youtube-dl
download = input("使用功能")

if download == "mp3" or download == "MP3":
    # 由於mp3需要先下載mp4之後使用ffmpeg工具轉檔,因此"ydl_opts"為轉檔的設定
    ydl_opts = {'format': 'bestaudio', 'postprocessors':
        [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '320'}]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:         # with功能為:如果有偵測到設定內容,則使用該設定來下載該網址的mp3檔案並在下載後清除設定值
        ydl.download([URL])
    print("mp3下載完成")

elif download == "mp4" or download == "MP4":
    with youtube_dl.YoutubeDL({'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]'}) as ydl: # 無須轉檔,直接設定下載mp4即可
        ydl.download([URL])
    print("mp4下載完成")
