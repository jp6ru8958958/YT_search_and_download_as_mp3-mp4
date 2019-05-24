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
        self.video_imagelink = []

    def get_search_info(self):
        HTML = requests.get(self.search_url).content
        soup = BeautifulSoup(HTML, "html.parser")
        video_name_soup = soup.select("h3 a")
        video_image_soup = soup.select("div.yt-thumb.video-thumb img")
        for get_info in range(20):
            self.video_name.append(video_name_soup[get_info].text)
            data = soup.select(".yt-lockup-meta-info")
            data = data[get_info].get_text("#").split("#")
            self.video_posttime.append(data[0])
            self.video_viewtimes.append(data[1])
            self.video_link.append("https://www.youtube.com" + video_name_soup[get_info]['href'])
            if get_info < 6:
                self.video_imagelink.append(video_image_soup[get_info]['src'])
            else:
                self.video_imagelink.append(video_image_soup[get_info]['data-thumb'])

    def delete_info(self):
        self.video_name = []
        self.video_link = []
        self.video_viewtimes = []
        self.video_posttime = []
        self.video_imagelink = []

    def print_info(self):
        print(len(self.video_name))
        print(self.video_name)
        print(len(self.video_posttime))
        print(self.video_posttime)
        print(len(self.video_viewtimes))
        print(self.video_viewtimes)
        print(len(self.video_link))
        print(self.video_link)
        print(len(self.video_imagelink))
        print(self.video_imagelink)

    def HTML_print(self):
        print(self.soup.prettify())


def open_browser():
    global downloadlink
    video_url = [downloadlink]
    webbrowser.open_new_tab(video_url)


def Mp3_download():
    global downloadlink
    label_Status['text'] = "Downloading......"
    video_url = downloadlink
    mp4_opts = {
        'format': 'bestaudio',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320'
        }]
    }
    with youtube_dl.YoutubeDL(mp4_opts) as ydl:
        ydl.download([video_url])
    label_Status['text'] = "Download finish!"


def Mp4_download():
    global downloadlink
    label_Status['text'] = "Downloading......"
    video_url = downloadlink
    mp3_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]'
    }
    with youtube_dl.YoutubeDL(mp3_opts) as ydl:
        ydl.download([video_url])
    label_Status['text'] = "Download finish!"


def Next_Button():
    global status, downloadlink
    if entry_Search.get()[0:8] == "https://":
        downloadlink = entry_Search.get()
        label_VideoName['text'] = "It is a video link, you can just click download button."
        label_VideoViewTimes['text'] = " "
        label_VideoPostTime['text'] = " "
        label_Status['text'] = " "
    else:
        Video_List = Video_Info(entry_Search.get())
        Video_List.get_search_info()
        if status == 0:
            label_VideoName['text'] = Video_List.video_name[status]
            label_VideoViewTimes['text'] = Video_List.video_viewtimes[status]
            label_VideoPostTime['text'] = Video_List.video_posttime[status]
            label_Status['text'] = " "
            downloadlink = Video_List.video_link[status]
        elif status > 0:
            if status == 20:
                status = 0
            label_VideoName['text'] = Video_List.video_name[status]
            label_VideoViewTimes['text'] = Video_List.video_viewtimes[status]
            label_VideoPostTime['text'] = Video_List.video_posttime[status]
            label_Status['text'] = " "
            downloadlink = Video_List.video_link[status]
        status += 1


def main():
    global entry_Search, status, label_VideoName, label_VideoViewTimes, label_EnterKeyWord, \
        label_VideoPostTime, label_Status, downloadlink
    status = 0

    main_window = tk.Tk()
    main_window.title('Youtube_Downloader')
    main_window.geometry('420x200')

    entry_read = StringVar()
    entry_Search = tk.Entry(main_window, width=25, bd=4, textvariable=entry_read)

    button_MP3_Download = tk.Button(main_window, text="MP3 download", width=10, height=2, command=Mp3_download)
    button_MP4_Download = tk.Button(main_window, text="MP4 download", width=10, height=2, command=Mp4_download)
    button_NEXT = tk.Button(main_window, text="NEXT", width=5, height=2, command=Next_Button)

    label_VideoName = Label(main_window)
    label_VideoViewTimes = Label(main_window)
    label_VideoPostTime = Label(main_window)
    label_Status = Label(main_window)
    label_EnterKeyWord = Label(main_window)
    label_EnterKeyWord["text"] = "Enter a keyword or link:"
    entry_Search.place(x=140, y=20, anchor='nw')
    label_EnterKeyWord.place(x=0, y=25, anchor='nw')
    label_VideoName.place(x=0, y=70, anchor='nw')
    label_VideoViewTimes.place(x=0, y=90, anchor='nw')
    label_VideoPostTime.place(x=0, y=110, anchor='nw')
    label_Status.place(x=0, y=150, anchor='nw')
    button_MP3_Download.place(x=180, y=135, anchor='nw')
    button_MP4_Download.place(x=300, y=135, anchor='nw')
    button_NEXT.place(x=335, y=10, anchor='nw')
    main_window.mainloop()


if __name__ == "__main__":
    main()
