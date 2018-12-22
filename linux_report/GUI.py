from tkinter import *                       #圖形介面的函式庫
import tkinter as tk

main_window = tk.Tk()
main_window.title('YOUTUBE_DOWNLOADER')     #設定視窗名稱
main_window.geometry('350x200')             #設定視窗大小

#FUNCTION===============================================================================================================

def button1_click():                                    #MP3下載按鈕
    key_word = main_entry.get()                         #取得輸入欄位的關鍵字
    show_label1["text"]='影片名稱:'+key_word
    show_label2["text"]='影片觀看次數:'+key_word

def button2_click():                                    #MP4下載按鈕
    key_word = main_entry.get()                         #取得輸入欄位的關鍵字
    show_label1["text"]='影片名稱:'+key_word
    show_label2["text"]='影片觀看次數:'+key_word

def button3_click():                                    #NEXT按鈕,確定搜索關鍵字
    key_word = main_entry.get()                         #取得輸入欄位的關鍵字
    show_label1["text"]=key_word

#TEXT ENTRY=============================================================================================================

entry_read=StringVar()                     #將entry_read變數(輸入的內容)設定為字串
main_entry = tk.Entry(main_window,width=25,bd=3,textvariable=entry_read)        #設定輸入框的大小並將關鍵字讀入entry功能裡

#BUTTON=================================================================================================================
#設定按鈕大小/按鈕輸出名稱          command為按下按鈕會觸發的函式名稱
button_one = tk.Button(main_window,text="MP3下載",width=10,height=2,command=button1_click)
button_two = tk.Button(main_window,text="MP4下載",width=10,height=2,command=button2_click)
button_three = tk.Button(main_window,text="NEXT",width=5,height=2,command=button3_click)

#LABEL==================================================================================================================
#顯示在程式中的字
show_label1=Label(main_window)
show_label2=Label(main_window)
main_label=Label(main_window)
main_label["text"] = "輸入關鍵字"

#PACK===================================================================
#設定所有功能在程式中的位置
main_entry.place(x=100, y=20, anchor='nw')
main_label.place(x=30, y=20 , anchor='nw')
show_label1.place(x=30, y=60, anchor='nw')
show_label2.place(x=30, y=90, anchor='nw')
button_one.place(x=100, y=150, anchor='nw')
button_two.place(x=200, y=150, anchor='nw')
button_three.place(x=300, y=25, anchor='nw')

main_window.mainloop()  #將所有程式包進一個主迴圈