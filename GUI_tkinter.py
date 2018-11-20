#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tkinter import *
import tkinter as tk

main_window = tk.Tk()
main_window.title('YOUTUBE_DOWNLOADER')
main_window.geometry('350x200')

#FUNCTION===============================================================================================================

def button1_click():
    key_word = main_entry.get()
    main_label["text"]="按鈕1"

def button2_click():
    key_word = main_entry.get()
    main_label["text"]="按鈕2"

#TEXT ENTRY=============================================================================================================

entry_read=StringVar()
main_entry = tk.Entry(main_window,width=20,textvariable=entry_read)

#BUTTON=================================================================================================================

button_one = tk.Button(main_window,text="按鈕1",width=10,height=2,command=button1_click)
button_two = tk.Button(main_window,text="按鈕2",width=10,height=2,command=button2_click)

#LABEL==================================================================================================================

main_label=Label(main_window)

#PACK===================================================================

main_entry.place(x=100, y=20, anchor='nw')
main_label.place(x=100, y=40, anchor='nw')
button_one.place(x=50, y=150, anchor='nw')
button_two.place(x=200, y=150, anchor='nw')
main_window.mainloop()