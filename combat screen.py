from tkinter import *


def avancer1():
    x11, y11, x12, y12 = canvas.coords(p1)
    if x11<391 :
        canvas.coords(p1, x11+100,y11, x12+100,y12)
    else :
        canvas.coords(p1, x11,y11, x12,y12)

def reculer1():
    x11, y11, x12, y12 = canvas.coords(p1)
    if x11>11:
        canvas.coords(p1, x11-100,y11, x12-100,y12)
    else:
        canvas.coords(p1, x11,y11, x12,y12)

def gauche1():
    x11, y11, x12, y12 = canvas.coords(p1)
    if y11>11:
        canvas.coords(p1, x11,y11-100, x12,y12-100)
    else:
        canvas.coords(p1, x11,y11, x12,y12)

def droite1():
    x11, y11, x12, y12 = canvas.coords(p1)
    if y12<489:
        canvas.coords(p1, x11,y11+100, x12,y12+100)
    else:
        canvas.coords(p1, x11,y11, x12,y12)


def reculer2():
    x21, y21, x22, y22 = canvas.coords(p2)
    if x21<1009:
        canvas.coords(p2, x21+100,y21, x22+100,y22)
    else:
        canvas.coords(p2, x21, y21, x22 ,y22)

def avancer2():
    x21, y21, x22, y22 = canvas.coords(p2)
    if x22>789:
        canvas.coords(p2, x21-100,y21, x22-100,y22)
    else:
        canvas.coords(p2, x21,y21, x22,y22)

def droite2():
    x21, y21, x22, y22 = canvas.coords(p2)
    if y21>11:
        canvas.coords(p2, x21,y21-100, x22,y22-100)
    else:
        canvas.coords(p2, x21, y21, x22 ,y22)

def gauche2():
    x21, y21, x22, y22 = canvas.coords(p2)
    if y22<489:
        canvas.coords(p2, x21,y21+100, x22,y22+100)
    else:
        canvas.coords(p2, x21,y21, x22,y22)


def grid(): #la grille de combat
    canvas.create_line(0, 100, 500, 100,fill='grey')
    canvas.create_line(0, 200, 500, 200,fill='grey')
    canvas.create_line(0, 300, 500, 300,fill='grey')
    canvas.create_line(0, 400, 500, 400,fill='grey')
    canvas.create_line(600, 100, 1100, 100,fill='grey')
    canvas.create_line(600, 200, 1100, 200,fill='grey')
    canvas.create_line(600, 300, 1100, 300,fill='grey')
    canvas.create_line(600, 400, 1100, 400,fill='grey')

    canvas.create_line(100, 0, 100,500,fill='grey')
    canvas.create_line(200, 0, 200,500,fill='grey')
    canvas.create_line(300, 0, 300,500,fill='grey')
    canvas.create_line(400, 0, 400,500,fill='grey')
    canvas.create_line(500, 0, 500,500,fill='grey')
    canvas.create_line(600, 0, 600,500,fill='grey')
    canvas.create_line(700, 0, 700,500,fill='grey')
    canvas.create_line(800, 0, 800,500,fill='grey')
    canvas.create_line(900, 0, 900,500,fill='grey')
    canvas.create_line(1000, 0, 1000,500,fill='grey')


def att1p1():
    x11, y11, x12, y12 = canvas.coords(p1)
    x21, y21, x22, y22 = canvas.coords(p2)
    at5=canvas.create_rectangle(x11+600, y11, x12+600, y12, fill='red2')
    dmg5=10
    if abs(x11+600-x21) < 10 and abs(y11-y21) < 10:
        fenetre.after(1, lambda : canvas.delete(at5))

def att1p2():
    x21, y21, x22, y22 = canvas.coords(p2)
    at21=canvas.create_rectangle(x21-5, y21, 0, y22, fill='blue')
    dmg2=20
    fenetre.after(625, lambda : canvas.delete(at21))


fenetre = Tk()

canvas= Canvas(fenetre, width=1100, height=500, background='black')
p1=canvas.create_oval(210, 210,290, 290,fill='red')
p2=canvas.create_oval(810, 210, 890, 290,fill='blue')
grid()


gauche1=Button(text="^",command=gauche1)
front1=Button(text=">",command=avancer1)
back1=Button(text="<",command=reculer1)
droite1=Button(text="v",command=droite1)
droite2=Button(text="^",command=droite2)
front2=Button(text="<",command=avancer2)
back2=Button(text=">",command=reculer2)
gauche2=Button(text="v",command=gauche2)
att1=Button(text="A",command=att1p1)
att2=Button(text="A", command=att1p2)


gauche1.grid(row=2,column=2)
front1.grid(row=3,column=3)
back1.grid(row=3,column=1)
droite1.grid(row=4,column=2)
att1.grid(row=3, column=2)
droite2.grid(row=2,column=6)
front2.grid(row=3,column=5)
back2.grid(row=3,column=7)
gauche2.grid(row=4,column=6)
att2.grid(row=3, column=6)
canvas.grid(row=1, column=4)

fenetre.mainloop()