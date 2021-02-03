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
import ast
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

def covid():
    url = "https://covid-19-data.p.rapidapi.com/country"

    querystring = {"name":country.get()}

    headers = {
        'x-rapidapi-key': "63bea75195msh836b9bb25a96cb1p124492jsn9b3f1b950c66",
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    try:
        r=response.json()
        info.config(font=('Helvetica','28'),text=
        f"В стране {r[0]['country']}:\nЗаражено: {r[0]['confirmed']}\nВ критическом состоянии: {r[0]['critical']}\nУмерло: {r[0]['deaths']}")
    except:
        info.config(text='Неверно введенная страна.')
    
def weather():
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q":position.get()}

    headers = {
        'x-rapidapi-key': "63bea75195msh836b9bb25a96cb1p124492jsn9b3f1b950c66",
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    r = ast.literal_eval(response.text)

    weatInfo.config(font=('Helvetica','28'),text=
        f'''Сейчас в {r["location"]["name"]}:
{r["current"]["condition"]["text"]}
Температура: {r["current"]["temp_c"]}C
Скорость ветра {r["current"]["wind_mph"]}м/c''')

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
tabs.add(tabs3,text="COVID-19")
tabs.add(tabs4,text="Weather")
tabs.pack()
#--------------укротитель ссылок-------------
shortw = Canvas(tabs1,width=600,height=600)
shortw.pack(expand=YES, fill=BOTH)
ent = Entry(tabs1)
shortw.create_window(300,300,window=ent)
but = Button(tabs1,command=short,text="Сократить ссылку.")
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
#-------------------COVID---------------------
covC = Canvas(tabs3,width=600,height=600)
covC.pack()
country = Entry(tabs3)
covC.create_window(300,500,window=country)
covB = Button(tabs3,text="Получить информацию.",command=covid)
covC.create_window(300,530,window=covB)
info = Label(tabs3)
covC.create_window(300,200,window=info)
#----------------WEATHER---------------------
weatC = Canvas(tabs4,width=600,height=600)
weatC.pack()
position = Entry(tabs4)
weatC.create_window(300,500,window=position)
weatB = Button(tabs4,command=weather,text='Получить текущую погоду.')
weatC.create_window(300,530,window=weatB)
weatInfo = Label(tabs4)
weatC.create_window(300,200,window=weatInfo)
#TODO: форкаст на х дней, ловитель ошибок и както сунуть файлы
label.bind("<Button-1>", lambda a: shortOpen(url))
main.mainloop()