from tkinter import *
import tkinter as tk
import requests
from bs4 import BeautifulSoup
import youtube_dl
import webbrowser

url = "https://www.youtube.com/results?search_query=" + str(input("輸入關鍵字") + "&sp=CAMSAhAB")

HTML = requests.get(url)
soup = BeautifulSoup(HTML.text, "html.parser")
video_name_soup = soup.select("h3 a")
video_image_soup = soup.select("div.yt-thumb.video-thumb img")

video_name = []
video_link = []
video_viewtimes = []
video_posttime = []
video_image = []

print(soup.prettify())

for get_info in range(20):
    video_name.append(video_name_soup[get_info].text)
    print(video_name_soup[get_info].text)
    data = soup.select(".yt-lockup-meta-info")
    data = data[get_info].get_text("#").split("#")
    video_posttime.append(data[0])
    video_viewtimes.append(data[1])
    video_link.append("https://www.youtube.com" + video_name_soup[get_info]['href'])
    if get_info < 6:
        video_image.append(video_image_soup[get_info]['src'])
    else:
        video_image.append(video_image_soup[get_info]['data-thumb'])

#    print("https://www.youtube.com" + video_name[get_info]['href'])
#    video_link[get_info] = "https://www.youtube.com" + video_name[get_info]['href']


print(len(video_name))
print(video_name)
print(len(video_posttime))
print(video_posttime)
print(len(video_viewtimes))
print(video_viewtimes)
print(len(video_link))
print(video_link)
print(len(video_image))
print(video_image)

#webbrowser.open_new_tab("https://www.youtube.com" + video_name[4]['href'])
