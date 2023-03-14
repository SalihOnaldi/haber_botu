#Dk 20 21 arası hatalı Ersoy'a sor


import feedparser
from tkinter import *
import webview
from datetime import datetime


def default_color_button():
    btn_son_dakika.configure(bg='lightblue')
    btn_dunya.configure(bg='lightblue')
    btn_ekonomi.configure(bg='lightblue')
    btn_saglık.configure(bg='lightblue')


def clear_frame():
    for widget in fr_haberler.winfo_children():
        widget.destroy()

def open_url(event):
    webview.create_window(event.widget.cget("text"), event.widget.cget("text"))
    webview.start()


def add_haberler(haberler):
    haber_count = 0

    for haber in haberler.entries:
        haber_count +=1
        if haber_count > 2 :
            break
        Label(fr_haberler, text =haber.title, anchor="w", font =("Helveticabold", 14 )).pack(side = TOP, fill="x")
        lbl_link = Label(fr_haberler, text =haber.link, anchor="w", font =("Helveticabold", 14 ),fg = "blue", cursor="hand2" )
        lbl_link.pack(side = TOP, fill="x")
        lbl_link.bind("<Button-1>", open_url)
        Label(fr_haberler, text ="-", anchor="c", font =("Helveticabold", 14 ),bg = "pink").pack(side = TOP, fill="x")


def son_dakika_command():
    clear_frame()
    default_color_button()
    btn_son_dakika.configure(bg='blue')
    for url in son_dakika_url: 
        print(url, datetime.now().time())
        haberler = feedparser.parse(url)
        print(url, datetime.now().time())
        add_haberler(haberler) 
    


def dunya_command():
    clear_frame()
    default_color_button()
    btn_dunya.configure(bg='blue')
    for url in dunya_url: 
        haberler = feedparser.parse(url)
        add_haberler(haberler) 


def ekonomi_command():
    clear_frame()
    default_color_button()
    btn_ekonomi.configure(bg='blue')
    for url in ekonomi_url: 
        haberler = feedparser.parse(url)
        add_haberler(haberler) 


def saglık_command():
    clear_frame()
    default_color_button()
    btn_saglık.configure(bg='blue')
    for url in saglık_url: 
        haberler = feedparser.parse(url)
        add_haberler(haberler) 


son_dakika_url = ["https://www.cnnturk.com/feed/rss/all/news",
                  "https://www.ensonhaber.com/rss/ensonhaber.xml",
                  "https://www.milliyet.com.tr/rss/rssnew/sondakikarss.xml",
                  "https://www.ahaber.com.tr/rss/anasayfa.xml"]



dunya_url =["https://www.cnnturk.com/feed/rss/dunya/news",
            "https://www.ensonhaber.com/rss/dunya.xml",
            "https://www.milliyet.com.tr/rss/rssnew/dunyarss.xml",
            "https://www.ahaber.com.tr/rss/dunya.xml"]


ekonomi_url = ["https://www.cnnturk.com/feed/rss/ekonomi/news",
                "https://www.ensonhaber.com/rss/ekonomi.xml",
                "https://www.milliyet.com.tr/rss/rssnew/ekonomirss.xml",
                "https://www.ahaber.com.tr/rss/video/ekonomi.xml"]



saglık_url = ["https://www.cnnturk.com/feed/rss/saglik/news",
              "https://www.ensonhaber.com/rss/ekonomi.xml",
              "https://www.milliyet.com.tr/rss/rssnew/teknolojirss.xml",
              "https://www.ahaber.com.tr/rss/saglik.xml"]





window = Tk()
window.title("Haber Bot Programı")
window.geometry("1000x600")


fr_haberler = Frame (window,  height=600)
fr_buttons = Frame (window, relief= RAISED, bg = "pink" , bd = 2)



btn_son_dakika = Button(fr_buttons, text="Son Dakika", font =("Helveticabold", 14 ),bg="lightblue", command=son_dakika_command)
btn_dunya = Button(fr_buttons, text="Dünya", font =("Helveticabold", 14 ),bg="lightblue", command=dunya_command)
btn_ekonomi = Button(fr_buttons, text="Ekonomi", font =("Helveticabold", 14 ),bg="lightblue", command=ekonomi_command)
btn_saglık = Button(fr_buttons, text="Sağlık", font =("Helveticabold", 14 ),bg="lightblue", command=saglık_command)


btn_son_dakika.grid(row = 0, column = 0, sticky= "ew", padx=5, pady=5)
btn_dunya.grid(row = 1, column = 0, sticky= "ew", padx=5, pady=5)
btn_ekonomi.grid(row = 2, column = 0, sticky= "ew", padx=5, pady=5)
btn_saglık.grid(row = 3, column = 0, sticky= "ew", padx=5, pady=5)


fr_buttons.grid (row= 0, column=0, sticky ="ns" )
fr_haberler.grid (row= 0, column=1, sticky ="nsew" )

window.mainloop()





