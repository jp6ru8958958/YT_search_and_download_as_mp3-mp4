from tkinter import *
import tkinter as tk
import requests
from bs4 import BeautifulSoup
import youtube_dl
import webbrowser


class Video_Info:
    def __init__(self, key_word):
        self.search_url = "https://www.youtube.com/results?search_query=" + key_word + "&sp=CAMSAhAB"
        self.video_name = []
        self.video_link = []
        self.video_viewtimes = []
        self.video_posttime = []

    def get_search_info(self):
        HTML = requests.get(self.search_url).content
        soup = BeautifulSoup(HTML, "html.parser")
        video_name_soup = soup.select("h3 a")
        for get_info in range(20):
            self.video_name.append(video_name_soup[get_info].text)
            data = soup.select(".yt-lockup-meta-info")
            data = data[get_info].get_text("#").split("#")
            self.video_posttime.append(data[0])
            self.video_viewtimes.append(data[1])
            self.video_link.append("https://www.youtube.com" + video_name_soup[get_info]['href'])

    def delete_info(self):
        self.video_name = []
        self.video_link = []
        self.video_viewtimes = []
        self.video_posttime = []

    def print_info(self):
        print(len(self.video_name))
        print(self.video_name)
        print(len(self.video_posttime))
        print(self.video_posttime)
        print(len(self.video_viewtimes))
        print(self.video_viewtimes)
        print(len(self.video_link))
        print(self.video_link)


def open_browser(video_url):
    webbrowser.open_new_tab(video_url)


def Mp4_download(video_url):
    mp4_opts = {
        'format': 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320'
        }]
    }
    with youtube_dl.YoutubeDL(mp4_opts) as ydl:
        ydl.download(video_url)


def Mp3_download(video_url):
    mp3_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]'
    }
    with youtube_dl.YoutubeDL(mp3_opts) as ydl:
        ydl.download(video_url)


def main():
    Video_list = Video_Info(str(input("輸入關鍵字：")))
    Video_list.get_search_info()
    Video_list.print_info()
    Video_list.delete_info()
    Video_list.print_info()


if __name__ == "__main__":
    main()
