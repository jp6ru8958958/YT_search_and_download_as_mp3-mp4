from tkinter import *
import tkinter as tk
import requests
from bs4 import BeautifulSoup
import youtube_dl
import webbrowser


url = "https://www.youtube.com/results?search_query=%E6%A0%B9%E6%9C%AC%E5%B0%B1"
HTML = requests.get(url)
soup = BeautifulSoup(HTML.text, "html.parser")
video_name = soup.select("h3 a")
for print_info in range(20):
    print(video_name[print_info].text)
    print(soup.select(".yt-lockup-video")[print_info-1].select(".yt-lockup-meta-info"))
    print("https://www.youtube.com" + video_name[print_info]['href'])


#webbrowser.open_new_tab("https://www.youtube.com" + video_name[4]['href'])
