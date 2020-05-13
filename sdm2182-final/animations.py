# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:43:55 2020

@author: shane
"""
from tkinter import *
from time import sleep
from PIL import Image, ImageDraw


def race():
    #tk = Tk()
    #canvas = Canvas(tk, width=1000, height=500)
    #tk.title("ENGI1006 Animation")
    #canvas.pack()

    img = Image.new("RGB",(1000,500))
    draw = ImageDraw.Draw(img)

    #ball1 = canvas.create_oval(0, 0, 20, 20, fill = "#A0E5C9")
    #ball2 = canvas.create_oval(0, 240, 20, 260, fill = "#629883")
    #ball3 = canvas.create_oval(0, 480, 20, 500, fill = "#2B5444")

    b1x1 = 0
    b1y1 = 0
    b1x2 = 20
    b1y2 = 20
    b2x1 = 0
    b2y1 = 240
    b2x2 = 20
    b2y2 = 260
    b3x1 = 0
    b3y1 = 480
    b3x2 = 20
    b3y2 = 500
    
    for i in range(50):
        #x1 = 20
        #x2 = 1.5*i
        #x3 = 0.2*(i**2)
        
        #canvas.move(ball1, x1, 0)
        #canvas.move(ball2, x2, 0)
        #canvas.move(ball3, x3, 0)
        #tk.update()
        sleep(0.04)
        
        b1x1 += 20
        b1x2 += 20
        b2x1 += 1.5*i
        b2x2 += 1.5*i
        b3x1 += 0.2*(i**2)
        b3x2 += 0.2*(i**2)
    
        draw.rectangle([(0,0),(1000,500)], fill = (255,255,255))    
        draw.ellipse([(b1x1,b1y1),(b1x2,b1y2)], fill = (160,229,201))
        draw.ellipse([(b2x1,b2y1),(b2x2,b2y2)], fill = (98,152,131))
        draw.ellipse([(b3x1,b3y1),(b3x2,b3y2)], fill = (43,84,68))
    
        filename = "static/animations/race" + str(i) +".png"
        img.save(filename)

    #tk.mainloop()

def race_gif():
    frames = []
    
    for i in range(50):
        filename = "static/animations/race" + str(i) + ".png"
        new_frame = Image.open(filename)
        frames.append(new_frame)

    frames[0].save('static/race.gif', save_all = True, append_images = frames[1:], 
           optimize = False, duration = 50, loop = 0)