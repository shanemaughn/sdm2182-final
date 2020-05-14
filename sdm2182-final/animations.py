# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:43:55 2020

@author: shane
"""
from tkinter import *
from time import sleep
from PIL import Image, ImageDraw
from math import sin,cos
from random import randint


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
    
def explosion():
    
    img = Image.new("RGB",(500,500))
    draw = ImageDraw.Draw(img)
    
    centers = [None]*12
    for i in range(len(centers)):
        centers[i] = randint(0, 500)
    
        

        
    angles = [None]*10
    x_shift = [None]*10
    y_shift = [None]*10
    for i in range(len(angles)):
        temp = randint(0, 360)
        angles[i] = temp * (6.283/360)
        x_shift[i] = int(10 * cos(angles[i]))
        y_shift[i] = int(10 * sin(angles[i]))
        
    ex1 = [None]*10
    ex2 = [None]*10
    ex3 = [None]*10
    ex4 = [None]*10
    ex5 = [None]*10
    ex6 = [None]*10
    ex01 = [None]*10
    ex02 = [None]*10
    ex03 = [None]*10
    ex04 = [None]*10
    ex05 = [None]*10
    ex06 = [None]*10
    
    shift1 = [None]*2
    shift2 = [None]*2
    shift3 = [None]*2
    shift4 = [None]*2
    shift5 = [None]*2
    shift6 = [None]*2
    
    for i in range(len(ex1)):
        ex1[i] = [centers[0],centers[1]]
        ex2[i] = [centers[2],centers[3]]
        ex3[i] = [centers[4],centers[5]]
        ex4[i] = [centers[6],centers[7]]
        ex5[i] = [centers[8],centers[9]]
        ex6[i] = [centers[10],centers[11]]
        
        ex01[i] = [centers[0]+3,centers[1]+3]
        ex02[i] = [centers[2]+1,centers[3]+1]
        ex03[i] = [centers[4]+4,centers[5]+4]
        ex04[i] = [centers[6]+5,centers[7]+5]
        ex05[i] = [centers[8]+7,centers[9]+7]
        ex06[i] = [centers[10]+5,centers[11]+5]

    
    
    for i in range(30):
        
        if i % 2 == 0:
            draw.rectangle([(0,0),(1000,500)], fill = (199,211,203))
        elif i % 3 == 0:
            draw.rectangle([(0,0),(1000,500)], fill = (211,211,211))
        elif i % 5 == 0:
            draw.rectangle([(0,0),(1000,500)], fill = (212,233,219))
        else:
            draw.rectangle([(0,0),(1000,500)], fill = (217,225,220))
            
        for j in range(len(ex1)):
            ex1[j][0] += x_shift[j]*i*0.1
            ex1[j][1] += y_shift[j]*i*0.1
            ex2[j][0] += x_shift[j]*i*0.8
            ex2[j][1] += y_shift[j]*i*0.8
            ex3[j][0] += x_shift[j]*i*0.5
            ex3[j][1] += y_shift[j]*i*0.5
            ex4[j][0] += x_shift[j]*(i**5)*(5*10**-6)
            ex4[j][1] += y_shift[j]*(i**5)*(5*10**-6)
            ex5[j][0] += x_shift[j]*(i**2)*0.02
            ex5[j][1] += y_shift[j]*(i**2)*0.02
            ex6[j][0] += x_shift[j]*(i**5)*(5*10**-6)
            ex6[j][0] += y_shift[j]*(i**5)*(5*10**-6)
            
            ex01[j][0] += x_shift[j]*i*0.1
            ex01[j][1] += y_shift[j]*i*0.1
            ex02[j][0] += x_shift[j]*i*0.8
            ex02[j][1] += y_shift[j]*i*0.8
            ex03[j][0] += x_shift[j]*i*0.5
            ex03[j][1] += y_shift[j]*i*0.5
            ex04[j][0] += x_shift[j]*(i**5)*(5*10**-6)
            ex04[j][1] += y_shift[j]*(i**5)*(5*10**-4)
            ex05[j][0] += x_shift[j]*(i**2)*0.02
            ex05[j][1] += y_shift[j]*(i**2)*0.02
            ex06[j][0] += x_shift[j]*(i**5)*(5*10**-6)
            ex06[j][1] += y_shift[j]*(i**5)*(5*10**-4)
            
            draw.ellipse([(ex1[j][0],ex1[j][1]),(ex01[j][0],ex01[j][1])], fill = (248,249,218))
            draw.ellipse([(ex2[j][0],ex2[j][1]),(ex02[j][0],ex02[j][1])], fill = (243,243,231))
            draw.ellipse([(ex3[j][0],ex3[j][1]),(ex03[j][0],ex03[j][1])], fill = (243,243,231))
            draw.ellipse([(ex4[j][0],ex4[j][1]),(ex04[j][0],ex04[j][1])], fill = (243,243,231))
            draw.ellipse([(ex5[j][0],ex5[j][1]),(ex05[j][0],ex05[j][1])], fill = (243,243,231))
            draw.ellipse([(ex6[j][1],ex6[j][0]),(ex06[j][1],ex06[j][0])], fill = (243,243,231))
        
        
        filename ='static/animations/explosion' + str(i) + '.png' 
        img.save(filename)
        
        
def explosion_gif(output_name):
    
    frames = []
    
    for i in range(30):
        filename = 'static/animations/explosion' + str(i) + '.png'
        new_frame = Image.open(filename)
        frames.append(new_frame)

    frames[0].save(output_name, save_all = True, append_images = frames[1:], 
           optimize = False, duration = 90, loop = 0)