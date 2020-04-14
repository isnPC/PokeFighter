from tkinter import *

def att1():
    x1, y11, x12, y12 = canvas.coords(p1)
    at11=canvas.create_rectangle(x11+600, y11, x12+600, y12, fill='red')
    fenetre.after(750, lambda : canvas.delete(at11))
    if abs(x11+600-x21) < 10 and abs(y11-y21) < 10:
        dmg1=24

def att2():
    x21, y21, x22, y22 = canvas.coords(p2)
    at2=canvas.create_rectangle(x21-5, y21, 0, y22, fill='blue')
    fenetre.after(625, lambda : canvas.delete(at21))
    if abs(x11+600-x21) < 10 :
        dmg1=20

def att3():
    x11, y11, x12, y12 = canvas.coords(p1)
    at3a=canvas.create_rectangle(x11, y11-100, 1100, y12-100, fill='red')
    at3b=canvas.create_rectangle(x11, y11+100, 1100, y12+100, fill='red')
    dmg=15
    fenetre.after(625, lambda : canvas.delete(at3a))
    fenetre.after(625, lambda : canvas.delete(at3b))

def att4():
    x11, y11, x12, y12 = canvas.coords(p1)
    at4=canvas.create_rectangle(x11+600, y11-100, x12+600, y12+100, fill='red')
    dmg=21
    fenetre.after(625, lambda : canvas.delete(at4))

def att5():                                                                     #en création
    x11, y11, x12, y12 = canvas.coords(p1)
    x21, y21, x22, y22 = canvas.coords(p2)
    at5=canvas.create_rectangle(x11+600, y11, x12+600, y12, fill='red')
    at51=canvas.create_line(x11+600,y11,x11+600,y12,fill='yellow')
    at52=canvas.create_line(x12+600,y11,x12+600,y12,fill='yellow')
    at53=canvas.create_line(x11+600,y11,x12+600,y11,fill='yellow')
    at54=canvas.create_line(x12+600,y12,x12+600,y12,fill='yellow')
    dmg5=10
    if canvas.coord(p2)==[x11+600, y11, x12+600, y12]:
        canvas.delete(at5)
        canvas.delete(at51)
        canvas.delete(at52)
        canvas.delete(at53)
        canvas.delete(at54)