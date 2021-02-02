#TODO: PIL with file open, WeatherAPI, LOL info, link shortner(can be replaced)
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
import sys, fileinput
from tkinter.messagebox import *
import requests
import json
import random
import webbrowser
from PIL import ImageTk, Image
#https://

def short():
  try:
    global url
    linkRequest = {
      "destination": f"https://{ent.get()}"
      , "domain": { "fullName": "rebrand.ly" }
      , "slashtag": f"itsshort_{random.randint(1,10000)*9999}"
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
        print("Long URL was %s, short URL is %s" % (link["destination"], link["shortUrl"]))
        url = link["shortUrl"]
        label.config(text=url)
  except:
    label.config(text="Неверная ссылка.")

def shortOpen(url):
  webbrowser.open_new(url)

def champInfo():
  try:
    champ = entC.get().capitalize()
    r = requests.get(f"http://ddragon.leagueoflegends.com/cdn/11.2.1/data/ru_RU/champion/{champ}.json")
    info = r.json()
    cLabel.insert(0.0,info["data"][champ]["lore"])
  except:
    cLabel.insert(0.0,"Неверно введенные данные")

def open_():
  global filef
  filef = askopenfilename()
  print(filef)
  photo = ImageTK.PhotoImage(Image.open(filef))
  pilC.create_image(50,10,anchor=NW,image=photo)

def rot():
  pass

main = Tk()
main.geometry("600x600")
main.title("something")

tabs = ttk.Notebook(main)

tabs1 = Frame(tabs)
tabs2 = Frame(tabs)
tabs3 = Frame(tabs)
tabs4 = Frame(tabs)
tabs.add(tabs1,text="Link short")
tabs.add(tabs2,text="League info")
tabs.add(tabs3,text="PIL")
tabs.add(tabs4,text="Weather")
tabs.pack()
#--------------укротитель ссылок-------------
shortw = Canvas(tabs1,width=600,height=600)
shortw.pack(expand=YES, fill=BOTH)
ent = Entry(tabs1)
shortw.create_window(300,300,window=ent)
but = Button(tabs1,command=short,text="Сократить ссылку")
shortw.create_window(300,340,window=but)
label = Label(tabs1)
shortw.create_window(300,200,window=label)
#--------------инфа по лиге------------------
leagueW = Canvas(tabs2,width=600,height=600)
leagueW.pack(expand=YES, fill=BOTH)
entC = Entry(tabs2)
leagueW.create_window(300,530,window=entC)
butt = Button(tabs2,text="Получить информацию о чемпионе.",command=champInfo)
leagueW.create_window(300,560,window=butt)
cLabel = Text(tabs2,width=60,height=30)
leagueW.create_window(300,250,window=cLabel)
#-------------------PIL---------------------
pilC = Canvas(tabs3,width=600,height=600)
pilC.pack(expand=YES, fill=BOTH)
rotB = Button(tabs3,text="Повернуть",command=rot)
pilC.create_window(300,560,window=rotB)
openB = Button(tabs3,text="Открыть фото.",command=open_)
pilC.create_window(300,540,window=openB)

label.bind("<Button-1>", lambda a: shortOpen(url))
main.mainloop()