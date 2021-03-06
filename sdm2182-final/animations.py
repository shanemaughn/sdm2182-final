# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:43:55 2020

@author: shane
"""
#######################################################
#   Name: Shane Maughn
#   UNI: sdm2182
#   
#   This module houses functions which generate 2 
#   animations.
#
######################################################

from tkinter import *
from time import sleep
from PIL import Image, ImageDraw
from math import sin,cos
from random import randint


def race():

    #initializes PIL window
    img = Image.new("RGB",(1000,500))
    draw = ImageDraw.Draw(img)

    #initializes starting positions for 3 balls
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
    
    #loop to simulate time
    for i in range(50):
        #shifts the x-components of each ball by intended equation
        b1x1 += 20
        b1x2 += 20
        b2x1 += 1.5*i
        b2x2 += 1.5*i
        b3x1 += 0.2*(i**2)
        b3x2 += 0.2*(i**2)
        
        #clears the screen
        draw.rectangle([(0,0),(1000,500)], fill = (255,255,255)) 
        #redraws new balls at updated locations
        draw.ellipse([(b1x1,b1y1),(b1x2,b1y2)], fill = (160,229,201))
        draw.ellipse([(b2x1,b2y1),(b2x2,b2y2)], fill = (98,152,131))
        draw.ellipse([(b3x1,b3y1),(b3x2,b3y2)], fill = (43,84,68))
        
        #saves current window as an image
        filename = "static/animations/race" + str(i) +".png"
        img.save(filename)


def race_gif():
    
    frames = []
    
    #opens each image and concatenates it to the frames list
    for i in range(50):
        filename = "static/animations/race" + str(i) + ".png"
        new_frame = Image.open(filename)
        frames.append(new_frame)
    
    #saves the images together as a gif
    frames[0].save('static/race.gif', save_all = True, append_images = frames[1:], 
           optimize = False, duration = 50, loop = 0)
    
def explosion():
    
    #initializes PIL window
    img = Image.new("RGB",(500,500))
    draw = ImageDraw.Draw(img)
    
    #randomly generates the 6 centers for the explosion
    centers = [None]*12
    for i in range(len(centers)):
        centers[i] = randint(0, 500)
    
    #initializes variables to house the angle each fragment leaves the explosion
    #and the corresponding x and y components of its unit vector
    angles = [None]*10
    x_shift = [None]*10
    y_shift = [None]*10
    
    #randomly generates the 10 angles and calculates corresponding values for
    #x_shift and y_shift
    for i in range(len(angles)):
        temp = randint(0, 360)
        angles[i] = temp * (6.283/360)
        x_shift[i] = int(10 * cos(angles[i]))
        y_shift[i] = int(10 * sin(angles[i]))
        
    #initializes arrays for the shards from each explosion
    #first co-ordinates
    ex1 = [None]*10
    ex2 = [None]*10
    ex3 = [None]*10
    ex4 = [None]*10
    ex5 = [None]*10
    ex6 = [None]*10
    #second co-ordinates
    ex01 = [None]*10
    ex02 = [None]*10
    ex03 = [None]*10
    ex04 = [None]*10
    ex05 = [None]*10
    ex06 = [None]*10

    
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

    
    #loop to simulate time
    for i in range(30):
        #changes background based on time in a haphazard way
        if i % 2 == 0:
            draw.rectangle([(0,0),(1000,500)], fill = (199,211,203))
        elif i % 3 == 0:
            draw.rectangle([(0,0),(1000,500)], fill = (211,211,211))
        elif i % 5 == 0:
            draw.rectangle([(0,0),(1000,500)], fill = (212,233,219))
        else:
            draw.rectangle([(0,0),(1000,500)], fill = (217,225,220))
            
        for j in range(len(ex1)):
            #adjusts first co-ordinate for each shard based on desired motion
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
            
            #adjusts second co-ordinate for each shard based on desired motion
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
            
            #redraws each ellipse
            draw.ellipse([(ex1[j][0],ex1[j][1]),(ex01[j][0],ex01[j][1])], fill = (248,249,218))
            draw.ellipse([(ex2[j][0],ex2[j][1]),(ex02[j][0],ex02[j][1])], fill = (243,243,231))
            draw.ellipse([(ex3[j][0],ex3[j][1]),(ex03[j][0],ex03[j][1])], fill = (243,243,231))
            draw.ellipse([(ex4[j][0],ex4[j][1]),(ex04[j][0],ex04[j][1])], fill = (243,243,231))
            draw.ellipse([(ex5[j][0],ex5[j][1]),(ex05[j][0],ex05[j][1])], fill = (243,243,231))
            draw.ellipse([(ex6[j][1],ex6[j][0]),(ex06[j][1],ex06[j][0])], fill = (243,243,231))
        
        #saves current window as an image
        filename ='static/animations/explosion' + str(i) + '.png' 
        img.save(filename)
        
        
def explosion_gif(output_name):
    
    frames = []
    
    #opens each image and concatenates it to the frames list
    for i in range(30):
        filename = 'static/animations/explosion' + str(i) + '.png'
        new_frame = Image.open(filename)
        frames.append(new_frame)
    
    #saves the frames list as a gif
    frames[0].save(output_name, save_all = True, append_images = frames[1:], 
           optimize = False, duration = 90, loop = 0)