from tkinter import *
from random import randint

def Bci():          #Les fonctions de choix du personnage
    choix=1
def Bme():
    choix=2
def Bma():
    choix=3
def Bbl():
    choix=4
def Bte():
    choix=5
def Bde():
    choix=6
def Bsa():
    choix=7
def Bla():
    choix=8
def Bga():
    choix=9
def Bex():
    choix=10
def Bdr():
    choix=11
def Brd():
    choix=randint(1, 11)


fenetre = Tk()

cizayox= Canvas(fenetre, width=100, height=100, background='red')    #Les differents canvas avec les images de chaques pokemons
megapagos= Canvas(fenetre, width=100, height=100, background='blue')
malamendre= Canvas(fenetre, width=100, height=100, background='black')
blizaroi= Canvas(fenetre, width=100, height=100, background='green')
tenefix= Canvas(fenetre, width=100, height=100, background='purple')
dedenne= Canvas(fenetre, width=100, height=100, background='yellow')
salarsen= Canvas(fenetre, width=100, height=100, background='pink')
lapyro= Canvas(fenetre, width=100, height=100, background='white')
gallame= Canvas(fenetre, width=100, height=100, background='teal')
excavarenne= Canvas(fenetre, width=100, height=100, background='brown')
dracolosse= Canvas(fenetre, width=100, height=100, background='orange')
rdm= Canvas(fenetre, width=100, height=100, background='gray')


Button(text="cizayox",command=Bci).grid(row=2,column=1) #Le placement de tous les objets
Button(text="megapagos",command=Bme).grid(row=2,column=2)
Button(text="malamendre",command=Bma).grid(row=2,column=3)
Button(text="blizaroi",command=Bbl).grid(row=2,column=4)
Button(text="tenefix",command=Bte).grid(row=4,column=1)
Button(text="dedenne",command=Bde).grid(row=4,column=2)
Button(text="salarsen",command=Bsa).grid(row=4,column=3)
Button(text="lapyro",command=Bla).grid(row=4,column=4)
Button(text="gallame",command=Bga).grid(row=6,column=1)
Button(text="excavarenne",command=Bex).grid(row=6,column=2)
Button(text="dracolosse",command=Bdr).grid(row=6,column=3)
Button(text="aléatoire",command=Brd).grid(row=6,column=4)
cizayox.grid(row=1,column=1)
megapagos.grid(row=1,column=2)
malamendre.grid(row=1,column=3)
blizaroi.grid(row=1,column=4)
tenefix.grid(row=3,column=1)
dedenne.grid(row=3,column=2)
salarsen.grid(row=3,column=3)
lapyro.grid(row=3,column=4)
gallame.grid(row=5,column=1)
excavarenne.grid(row=5,column=2)
dracolosse.grid(row=5,column=3)
rdm.grid(row=5,column=4)

fenetre.mainloop()

