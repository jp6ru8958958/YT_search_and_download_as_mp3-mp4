from tkinter import *
import tkinter as tk
import requests
from bs4 import BeautifulSoup
import youtube_dl

main_window = tk.Tk()
main_window.title('YOUTUBE_DOWNLOADER')
main_window.geometry('550x200')

features=['video',0,'key_word']

#FUNCTION===============================================================================================================
def button3_click():
    key_word = main_entry.get()
    if features[2] != key_word:
        features[1]=0
    features[2]=key_word
    url = "https://www.youtube.com/results?sp=CAM%253D&search_query="+key_word
    request = requests.get(url)
    content = request.content
    soup = BeautifulSoup(content, "html.parser")
    video_name = soup.select(".yt-lockup-video")[features[1]].select("a[rel='spf-prefetch']")
    video_watchtimes = soup.select(".yt-lockup-video")[features[1]].select(".yt-lockup-meta-info")

    features[0]=("https://www.youtube.com{}".format(video_name[0].get("href")))
    features[1]+=1

    show_label1["text"]='影片名稱:'+video_name[0].get("title")
    show_label2["text"]="發佈時間"+video_watchtimes[0].get_text(" ")

def button1_click():
    ydl_opts = {'format': 'bestaudio', 'postprocessors':
        [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '320'}]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([features[0]])
    print("mp3下載完成")

def button2_click():
    with youtube_dl.YoutubeDL({'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]'}) as ydl:
        ydl.download([features[0]])
    print("mp4下載完成")


#TEXT ENTRY=============================================================================================================

entry_read=StringVar()
main_entry = tk.Entry(main_window,width=25,bd=3,textvariable=entry_read)

#BUTTON=================================================================================================================

button_one = tk.Button(main_window,text="MP3下載",width=10,height=2,command=button1_click)
button_two = tk.Button(main_window,text="MP4下載",width=10,height=2,command=button2_click)
button_three = tk.Button(main_window,text="NEXT",width=5,height=2,command=button3_click)

#LABEL==================================================================================================================


show_label1=Label(main_window)
show_label2=Label(main_window)
main_label=Label(main_window)
main_label["text"] = "輸入關鍵字"

#PACK===================================================================

main_entry.place(x=200, y=20, anchor='nw')
main_label.place(x=130,y=20,anchor='nw')
show_label1.place(x=10, y=70, anchor='nw')
show_label2.place(x=10, y=100, anchor='nw')
button_one.place(x=200, y=150, anchor='nw')
button_two.place(x=300, y=150, anchor='nw')
button_three.place(x=400, y=25, anchor='nw')
main_window.mainloop()