# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

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
    return render_template("sdm2182_chess.html")

#start the server
if __name__ == "__main__":
    app.run()