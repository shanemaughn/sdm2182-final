# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""
#######################################################
#   Name: Shane Maughn
#   UNI: sdm2182
#   
#   This program uses Flask to serve a main webpage,
#   an animations page and a chess page
#
######################################################

#import statements
from flask import Flask, render_template
from animations import  race, race_gif, explosion, explosion_gif
import datetime, time
import pandas as pd
import requests
import bs4

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("sdm2182_mainpage.html")

@app.route("/animation")
def animate():
    return render_template("sdm2182_animate.html")

@app.route("/chess")
def chess():

    #store current time in the format hour: minute: time    
    time = str(datetime.datetime.now().hour) + ':' + \
    str(datetime.datetime.now().minute) + ':' + str(datetime.datetime.now().second)
    
    #Generates welcome message based on time of day
    x = datetime.datetime.now().hour
    if x < 12:
        message = "Good Morning Shane. Here is your update:"
    elif x < 16:
        message = "Good Afternoon Shane. Here is your update:"
    elif x < 20:
        message =  "Good Evening Shane. Here is your update:"
    else:
         message = "Good Night Shane. Here is your update:"
         
    #converts ranking info from webpage into pandas DataFrame
    country_info = bs4.BeautifulSoup\
    (requests.get('https://ratings.fide.com/topfed.phtml?tops=0&ina=2&country=BAR')\
     .content,'lxml')
    country_tables = country_info.find_all('table')
    temp = pd.read_html(str(country_tables[1]))
    rankings = temp[4]
    
    #finds current ranking 
    pos = int(rankings[rankings[1]=='Maughn, Shane'].index.values)
    
    #creates DataFrames for those players closest above and closest below
    threats= pd.DataFrame()
    threats["Name"] = rankings.iloc[pos+1:pos+4,1]
    threats["Rating"] = rankings.iloc[pos+1:pos+4,4]
    
    targets= pd.DataFrame()
    targets["Name"] = rankings.iloc[pos-3:pos,1]
    targets["Rating"] = rankings.iloc[pos-3:pos,4]
    
    #converts personal chess statistics into a pandas DataFrame
    personal_info =bs4.BeautifulSoup\
    (requests.get('https://ratings.fide.com/card.phtml?event=11103310').content,'lxml')
    personal_tables = personal_info.find_all('table')
    data = pd.read_html(str(personal_tables[5]))
    temp = data[0].iloc[3,2]
    temp = temp.split()
    personal_data = pd.DataFrame([["Std. Rating:", "Blitz Rating:", "Title:", "Fed:"],\
                                 [temp[0][4:],temp[3][5:],data[0].iloc[2,2],data[0].iloc[1,2]]]\
                                 ,index = ["0","1"]).T

    #converts tournaments listing into a pandas DataFrame
    tournament_info =bs4.BeautifulSoup\
    (requests.get('https://ratings.fide.com/tournament_list.phtml?moder=ev_code&country=USA')\
     .content,'lxml')
    tournament_tables = tournament_info.find_all('table')
    temp = pd.read_html((str(tournament_tables[1])))
    
    #selects the 5 closest tournaments to display
    tournaments = temp[3].iloc[1:6, 2:4]
    tournaments.columns = ["Name","Location"] 
         
    #returns required variables to html file
    pos=str(pos)
    return render_template("sdm2182_chess.html", time=time, message=message, \
                           pos=pos, threats=threats.to_html(classes='data'), \
                           targets=targets.to_html(classes='data'), \
                           personal_data=personal_data, \
                           tournaments=tournaments.to_html(classes='data'))
 


#start the server
if __name__ == "__main__":
    
    print("Animations Generating...")
    
    #generates animations and saves them as gifs
    race()
    race_gif()
    explosion()
    explosion_gif('static/explosion1.gif')
    explosion()
    explosion_gif('static/explosion2.gif')
    
    app.run()