from tkinter import *


def avancer1():
    x11, y11, x12, y12 = canvas.coords(p1)
    canvas.coords(p1, x11+10,y11, x12+10,y12)

def reculer1():
    x11, y11, x12, y12 = canvas.coords(p1)
    canvas.coords(p1, x11-10,y11, x12-10,y12)

def sauter1():
    x11, y11, x12, y12 = canvas.coords(p1)
    canvas.coords(p1, x11+1,y11-15, x12+1,y12-15)
    canvas.coords(p1, x11,y11+15, x12,y12+15)

def at1():
    x11, y11, x12, y12 = canvas.coords(p1)
    canvas.create_line(x11+12, y11, x12+2, y12, fill='red')

def reculer2():
    x21, y21, x22, y22 = canvas.coords(p2)
    canvas.coords(p2, x21+10,y21, x22+10,y22)

def avancer2():
    x21, y21, x22, y22 = canvas.coords(p2)
    canvas.coords(p2, x21-10,y21, x22-10,y22)

def sauter2():
    x21, y21, x22, y22 = canvas.coords(p2)
    canvas.coords(p2, x21+1,y21-15, x22+1,y22-15)
    canvas.coords(p2, x21,y21+15, x22,y22+15)

def at2():
    x21, y21, x22, y22 = canvas.coords(p2)
    canvas.create_line(x21-2, y21, x22-12, y22, fill='blue')


fenetre = Tk()

canvas= Canvas(fenetre, width=250, height=75, background='black')
p1=canvas.create_oval(0, 55, 10, 75,fill='red')
p2=canvas.create_oval(240, 55, 250, 75,fill='blue')

infocombatJ1=Canvas(fenetre, width=75, height=75, background='red')
infocombatJ2=Canvas(fenetre, width=75, height=75, background='blue')

jump1=Button(text="^",command=sauter1)
front1=Button(text=">",command=avancer1)
back1=Button(text="<",command=reculer1)
att1=Button(text="A",command=at1)

jump2=Button(text="^",command=sauter2)
front2=Button(text="<",command=avancer2)
back2=Button(text=">",command=reculer2)
att2=Button(text="A",command=at2)

canvas.grid(row=1, column=5)
infocombatJ1.grid(row=2, column=4)
infocombatJ2.grid(row=2, column=6)
att1.grid(row=3,column=2)
att2.grid(row=3,column=8)
jump1.grid(row=4,column=2)
front1.grid(row=4,column=3)
back1.grid(row=4,column=1)
jump2.grid(row=4,column=8)
front2.grid(row=4,column=7)
back2.grid(row=4,column=9)


fenetre.mainloop()