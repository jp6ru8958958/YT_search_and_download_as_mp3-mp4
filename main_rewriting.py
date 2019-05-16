from tkinter import *
import tkinter as tk
import requests
from bs4 import BeautifulSoup
import youtube_dl
import webbrowser


class Video_Info:
    def __init__(self, key_word):
        self.url = "https://www.youtube.com/results?sp=CAM%253D&search_query=" + key_word
        self.name = "none"
        self.owner = "none"

    def get_video_info(self):
        url = "https://www.youtube.com/results?search_query=%E6%A0%B9%E6%9C%AC%E5%B0%B1"
        HTML = requests.get(url).content
        soup = BeautifulSoup(HTML, "html.parser")


    def open_browser(self):
        webbrowser.open_new_tab(self.url)


def Mp4_download(Select_url):
    mp4_opts = {
        'format': 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320'
        }]
    }
    with youtube_dl.YoutubeDL(mp4_opts) as ydl:
        ydl.download(Select_url)
    print("mp3下載完成")


def Mp3_download(Select_url):
    mp3_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]'
    }
    with youtube_dl.YoutubeDL(mp3_opts) as ydl:
        ydl.download(Select_url)
    print("mp4下載完成")




def main():
    Video = Video_Info(str(input("輸入關鍵字：")))


if __name__ == "__main__":
    main()
