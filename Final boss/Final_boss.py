#TODO: PIL with file open, WeatherAPI, LOL info, link shortner(can be replaced)
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.filedialog import *
import sys, fileinput
from tkinter.messagebox import *
import requests
import json
import random
#https://
def short():
    linkRequest = {
      "destination": f"{ent.get()}"
      , "domain": { "fullName": "rebrand.ly" }
      , "slashtag": f"itsshort_{random.randint(1,10000)*9999}"
      , "title":"How to burn 10M"
    }

    requestHeaders = {
      "Content-type": "application/json",
      "apikey": "e94e1323b3a648c5bd55e4e2c20e5085"
    }

    r = requests.post("https://api.rebrandly.com/v1/links", 
        data = json.dumps(linkRequest),
        headers=requestHeaders)
    print(r)
    if (r.status_code == requests.codes.ok):
        link = r.json()
        print(link)
        print("Long URL was %s, short URL is %s" % (link["destination"], link["shortUrl"]))

main = Tk()
main.geometry("600x600")
main.title("something")

tabs = ttk.Notebook(main)
text=[1,2,3,4]

tabs1 = Frame(tabs)
tabs2 = Frame(tabs)
tabs3 = Frame(tabs)
tabs4 = Frame(tabs)
tabs.add(tabs1,text="Link short")
tabs.add(tabs2,text="League info")
tabs.add(tabs3,text="PIL")
tabs.add(tabs4,text="Weather")
tabs.pack()

w1 = Canvas(tabs1,width=600,height=600)
w1.pack()

ent = Entry(tabs1)
w1.create_window(300,300,window=ent)

but = Button(tabs1,command=short)
w1.create_window(300,320,window=but)

main.mainloop()