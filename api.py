from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


source = requests.get('https://www.biospectrumindia.com/news/83/16116/coronavirus-covid-19-cases-in-india-state-wise-daily-updates-tracker.html').text

soup = BeautifulSoup(source, 'lxml')
# print(soup)
table= soup.find('table', { 'class' : 'medium css-yrgpw8 svelte-lgwtoo striped compact desktop-only' })
rows=table.findAll('tr',class_='css-kfswhc svelte-lgwtoo')

data=[]
for l,j in enumerate(rows):
    if(l!=0):
        cols=j.findAll('td')
        data.append([str(i.text.replace(',',"")) for i in cols])

df = pd.DataFrame(data, columns = ['State', 'Cases','Cured','Death'])



def plotPie():
    labels =(df['State'])
    values=df['Cases']
    values=[i.replace(",", "") for i in values]
    print(values)

    explode = list()
    for k in labels:
        explode.append(0.1)


    root= tk.Tk()
    actualFigure = plt.figure(figsize=(40,15), dpi=100)
    actualFigure.suptitle("Corona Stats", fontsize = 22)
    pie = plt.pie(values, labels=labels, explode=explode, shadow=True, autopct='%1.1f%%')
    # plt.legend(pie[0], labels, loc="upper left")  
    canvas = FigureCanvasTkAgg(actualFigure, root)
    canvas.get_tk_widget().pack()
    root.mainloop()

plotPie()