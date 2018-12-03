from tkinter import *
import tkinter as tk

main_window = tk.Tk()
main_window.title('YOUTUBE_DOWNLOADER')
main_window.geometry('350x200')

#FUNCTION===============================================================================================================

def button1_click():
    key_word = main_entry.get()
    url = "https://www.youtube.com/results?sp=CAM%253D&search_query=" + key_word
    show_label1["text"]='影片名稱:'+key_word
    show_label2["text"]='影片觀看次數:'+key_word

def button2_click():
    key_word = main_entry.get()
    show_label1["text"]='影片名稱:'+key_word
    show_label2["text"]='影片觀看次數:'+key_word

def button3_click():
    key_word = main_entry.get()
    show_label1["text"]=key_word

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

main_entry.place(x=100, y=20, anchor='nw')
main_label.place(x=30,y=20,anchor='nw')
show_label1.place(x=30, y=60, anchor='nw')
show_label2.place(x=30, y=90, anchor='nw')
button_one.place(x=100, y=150, anchor='nw')
button_two.place(x=200, y=150, anchor='nw')
button_three.place(x=300, y=25, anchor='nw')
main_window.mainloop()