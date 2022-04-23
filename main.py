from __future__ import print_function

import email.utils
import textwrap
from db import Database
from tkinter import messagebox
import eel
from flask import Flask
import io
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import webbrowser
from tkinter import filedialog
from tkinter import ttk
import cv2
import imutils
import argparse
import os
import numpy as np
import torch
import torch.backends.cudnn as cudnn
from tkhtmlview import HTMLLabel
from tkhtmlview import *
import tkhtmlview

eel.init("web")


HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

db = Database('store.db')

#@eel.expose
def next(event):
    print("Willkommen auf der nächsten Seite")

'''exitimg = Image.open("back.jpg").resize((20,20), Image.ANTIALIAS)
nextimg = Image.open("next.jpg").resize((20,20), Image.ANTIALIAS)
exitimgres = ImageTk.PhotoImage(nextimg)
nextimgres = ImageTk.PhotoImage(exitimg)'''


'''def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)'''

window = tk.Tk()
window.title(" Events Darmstadt ")
window.geometry("1200x800")
bgimg = Image.open("bgimg.jpg")
bgimg2 = ImageTk.PhotoImage(bgimg)
bglabel = tk.Label(window, image=bgimg2)
bglabel.place(x=0, y=0, relheight=1, relwidth=1)
mylabel = tk.Label(window,
                   text="Sagen Sie uns bitte, welches Event Sie diese Woche besuchen möchten, damit wir",
                   font=('Arial bold', 16))
mylabel.place(x=10, y=80)

mylabel1 = tk.Label(window, text="für Sie nach verfügbaren Plätzen suchen können!", font=('Arial bold', 16))
mylabel1.place(x=10, y=120)

# frame = Frame(window, width=600, height=400)
image = Image.open("imageonline-co-split-image.jpg")
rszimage1 = image.resize((200, 200), Image.ANTIALIAS)
radioimage1 = ImageTk.PhotoImage(rszimage1)
image2 = Image.open("imageonline-co-split-image (1).jpg")
rszimage2 = image2.resize((200, 200), Image.ANTIALIAS)
radioimage2 = ImageTk.PhotoImage(rszimage2)
image3 = Image.open("images.jpg")
rszimage3 = image3.resize((200, 200), Image.ANTIALIAS)
radioimage3 = ImageTk.PhotoImage(rszimage3)
image4 = Image.open("uncharted.jpg")
rszimage4 = image4.resize((200, 200), Image.ANTIALIAS)
radioimage4 = ImageTk.PhotoImage(rszimage4)

pb = ttk.Progressbar(window, orient='horizontal', mode='determinate', length=400)
pb.place(x=400, y=20)
pb['value'] = 0

v = IntVar()
radio1 = tk.Radiobutton(window, variable=v, value=1, image=radioimage1)
radio2 = tk.Radiobutton(window, variable=v, value=2, image=radioimage2)
radio3 = tk.Radiobutton(window, variable=v, value=3, image=radioimage3)
radio4 = tk.Radiobutton(window, variable=v, value=4, image=radioimage4)
radio1.place(x=50, y=200)
radio2.place(x=50, y=400)
radio3.place(x=400, y=200)
radio4.place(x=400, y=400)


# eel.init('web')
# eel.start('main.html')


def facebook(event):
    webbrowser.open_new_tab(r"https://www.facebook.com/profile.php?id=100079921523267")


def insta(event):
    webbrowser.open_new_tab(r"http://www.instagram.com")


def facebookgroup(event):
    webbrowser.open_new_tab(r"https://www.facebook.com/groups/1199278287578892")


def openNewWindow():
    newWindow = tk.Toplevel(window)

    newWindow.title("Namenabfrage")
    newWindow.geometry("1200x800")
    namenlabel = tk.Label(newWindow,
                          text="Bitte geben Sie hier den Namen und die Email-Adresse von sich und Ihren Freunden an,",
                          font=('Arial bold', 16))
    namenlabel.place(x=10, y=80)
    namenlabel2 = tk.Label(newWindow, text='die mit Ihnen zum Event gehen sollen', font=('Arial Bold', 16))
    namenlabel2.place(x=10, y=120)

    def add():
        db.insert(name1.get(), birth1.get(), email1.get(), name2.get(), birth2.get(), email2.get(), name3.get(),
                  birth3.get(), email3.get(), name4.get(), birth4.get(), email4.get())

    button_next = tk.Button(newWindow, text="Nächste Seite",
                            command=lambda: [print(name1.get()), print(email1.get()), add(), openNewWindow2(),
                                             newWindow.destroy()])
    button_next.bind()
    button_next.place(x=700, y=600)

    buttonQuit2 = tk.Button(newWindow, text="Exit", command=window.destroy)
    buttonQuit2.place(x=800, y=600)
    pb2 = ttk.Progressbar(newWindow, orient='horizontal', mode='determinate', length=400)
    pb2.place(x=400, y=20)
    pb2['value'] = 20

    sociallabel = tk.Label(newWindow, text="Und loggen Sie sich zusätzlich auf einer Social Media Platform ein, "
                           , font=("Arial Bold", 16))
    sociallabel.place(x=10, y=370)
    sociallabel2 = tk.Label(newWindow, text='um extra Informationen und Angebote erhalten zu können', font=('Arial Bold'
                                                                                                            , 16))
    sociallabel2.place(x=10, y=410)
    name1 = tk.StringVar()
    nameneintrag = tk.Frame(newWindow)
    nameneintrag.place(x=100, y=170)
    name_label = tk.Label(nameneintrag, text="Dein Name:")
    name_label.pack(fill='x', expand=True)
    name_entry = tk.Entry(nameneintrag, textvariable=name1)
    name_entry.pack(fill='x', expand=True)

    name2 = tk.StringVar()
    nameneintrag2 = tk.Frame(newWindow)
    nameneintrag2.place(x=400, y=170)
    name2_label = tk.Label(nameneintrag2, text="Namen der Freunde:")
    name2_label.pack(fill='x', expand=True)
    name2_entry = tk.Entry(nameneintrag2, textvariable=name2)
    name2_entry.pack(fill='x', expand=True)

    name3 = tk.StringVar()

    nameneintrag3 = tk.Frame(newWindow)
    nameneintrag3.place(x=550, y=170)
    name_label3 = tk.Label(nameneintrag3)
    name_label3.pack(fill='x', expand=True)
    name_entry3 = tk.Entry(nameneintrag3, textvariable=name3)
    name_entry3.pack(fill='x', expand=True)

    name4 = tk.StringVar()

    nameneintrag4 = tk.Frame(newWindow)
    nameneintrag4.place(x=700, y=170)
    name_label4 = tk.Label(nameneintrag4)
    name_label4.pack(fill='x', expand=True)
    name_entry4 = tk.Entry(nameneintrag4, textvariable=name4)
    name_entry4.pack(fill='x', expand=True)

    email1 = tk.StringVar()
    emaileintrag = tk.Frame(newWindow)
    emaileintrag.place(x=100, y=220)
    email_label = tk.Label(emaileintrag, text="Deine Email-Adresse:")
    email_label.pack(fill='x', expand=True)
    email_entry = tk.Entry(emaileintrag, textvariable=email1)
    email_entry.pack(fill='x', expand=True)
    email_entry.focus()

    email2 = tk.StringVar()
    emaileintrag2 = tk.Frame(newWindow)
    emaileintrag2.place(x=400, y=220)
    email2_label = tk.Label(emaileintrag2, text="Email der Freunde:")
    email2_label.pack(fill='x', expand=True)
    email2_entry = tk.Entry(emaileintrag2, textvariable=email2)
    email2_entry.pack(fill='x', expand=True)

    email3 = tk.StringVar()
    emaileintrag3 = tk.Frame(newWindow)
    emaileintrag3.place(x=550, y=220)
    email_label3 = tk.Label(emaileintrag3)
    email_label3.pack(fill='x', expand=True)
    email_entry3 = tk.Entry(emaileintrag3, textvariable=email3)
    email_entry3.pack(fill='x', expand=True)

    email4 = tk.StringVar()
    emaileintrag4 = tk.Frame(newWindow)
    emaileintrag4.place(x=700, y=220)
    email_label4 = tk.Label(emaileintrag4)
    email_label4.pack(fill='x', expand=True)
    email_entry4 = tk.Entry(emaileintrag4, textvariable=email4)
    email_entry4.pack(fill='x', expand=True)

    birth1 = tk.StringVar()
    birtheintrag1 = tk.Frame(newWindow)
    birtheintrag1.place(x=100, y=270)
    birth_label1 = tk.Label(birtheintrag1, text="Geburtsdatum:")
    birth_label1.pack(fill='x', expand=True)
    birth_entry1 = tk.Entry(birtheintrag1, textvariable=birth1)
    birth_entry1.pack(fill='x', expand=True)

    birth2 = tk.StringVar()
    birtheintrag2 = tk.Frame(newWindow)
    birtheintrag2.place(x=400, y=270)
    birth_label2 = tk.Label(birtheintrag2)
    birth_label2.pack(fill='x', expand=True)
    birth_entry2 = tk.Entry(birtheintrag2, textvariable=birth2)
    birth_entry2.pack(fill='x', expand=True)

    birth3 = tk.StringVar()
    birtheintrag3 = tk.Frame(newWindow)
    birtheintrag3.place(x=550, y=270)
    birth_label3 = tk.Label(birtheintrag3)
    birth_label3.pack(fill='x', expand=True)
    birth_entry3 = tk.Entry(birtheintrag3, textvariable=birth3)
    birth_entry3.pack(fill='x', expand=True)

    birth4 = tk.StringVar()
    birtheintrag4 = tk.Frame(newWindow)
    birtheintrag4.place(x=700, y=270)
    birth_label4 = tk.Label(birtheintrag4)
    birth_label4.pack(fill='x', expand=True)
    birth_entry4 = tk.Entry(birtheintrag4, textvariable=birth4)
    birth_entry4.pack(fill='x', expand=True)

    instabutton = tk.Button(newWindow, text="Instagram", bg="cyan")
    facebookbutton = tk.Button(newWindow, text="Facebook", bg="light blue")
    instabutton.place(x=250, y=480)
    facebookbutton.place(x=450, y=480)
    instabutton.bind("<Button-1>", insta)
    facebookbutton.bind("<Button-1>", facebook)

    #@eel.expose
    def add():
        db.insert(name1.get(), birth1.get(), email1.get(), name2.get(), birth2.get(), email2.get(), name3.get(),
                  birth3.get(), email3.get(), name4.get(), birth4.get(), email4.get())


buttonQuit = tk.Button(window, text="Exit", compound=LEFT, command=window.destroy)
buttonQuit.place(x=800, y=650)
button_name = tk.Button(window, text="Next", compound=LEFT, command=lambda: [openNewWindow(), window.withdraw()])
button_name.bind("<Button-1>", next)
button_name.place(x=850, y=650)


def openNewWindow2():
    newWindow2 = tk.Toplevel(window)
    newWindow2.title("Altersabfrage")
    newWindow2.geometry("1200x800")
    taglabel = Label(newWindow2,
                     text="Teilen Sie hier oder auf der Social Media Seite von uns ein Foto von Euch beim Event und nehmt dadurch am Gewinnspiel teil",
                     font=('Arial bold', 16))
    taglabel.grid(column=0, row=0)

    #@eel.expose()
    def upload():
        f_types = [('Jpg Files', '*.jpg'),
                   ('PNG Files', '*.png'),
                   ('WebP Files', '*.webp')]
        filename = tk.filedialog.askopenfilename(multiple=True, filetypes=f_types)
        filenametest = " ".join(str(x) for x in filename)

        imagecount = cv2.imread(filenametest)

        for f in filename:
            img = Image.open(f)
            img = img.resize((600, 400))
            img = ImageTk.PhotoImage(img)
            e1 = tk.Label(newWindow2)
            e1.place(x=100, y=100)
            e1.image = img
            e1['image'] = img

        (regions, _) = HOGCV.detectMultiScale(imagecount, winStride=(4, 4), padding=(4, 4), scale=1.05)
        count = 0
        for (x, y, w, h) in regions:
            cv2.rectangle(imagecount, (x, y), (x + w, y + h), (0, 0, 255), 2)
            count += 1
        print(count)

    uploadbutton = tk.Button(newWindow2, text="Bild hochladen", command=lambda: upload())
    uploadbutton.place(width=200, height=100, x=100, y=100)
    buttonnext = tk.Button(newWindow2, text="Nächste Seite", command=lambda: [openNewWindow3(), newWindow2.destroy()])
    buttonnext.place(x=730, y=300)
    butttest = tk.Button(newWindow2, text="Exit", command=lambda: window.destroy())
    butttest.place(x=730, y=340)

'''@eel.expose()
def multiply(inti, intj):
    return inti*intj
'''

def openNewWindow3():
    newWindow3 = tk.Toplevel(window)
    newWindow3.title("Test")
    newWindow3.geometry("1200x800")
    finalbutton = tk.Button(newWindow3, text='Verlassen', command=lambda: [window.destroy()])
    finalbutton.place(x=300, y=300)

#eel.start("main.html")
tk.mainloop()
