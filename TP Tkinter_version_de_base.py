from tkinter import *
from random import *

nim = Tk()
nim.geometry('1380x650')
nim.title('Jeu de Nim')
nim.resizable(width = False,height = False)
type_jeu_machine = True
type_dahut = False
fic_all =  PhotoImage(file = 'allumette.png')
img_all = []
fic_com = [PhotoImage(file = 'im_b1.png'), PhotoImage(file = 'im_b2.png'), PhotoImage(file = 'im_b3.png')]
b_com = []
fic_go = PhotoImage(file = 'Image_go.png')
b_go = None
fic_humain = PhotoImage(file = 'Image_joueur.png')
b_humain = None
fic_bot = PhotoImage(file = 'Image_bot.png')
b_bot = None
fic_intelligent = PhotoImage(file = 'AI.png')
b_intelligent = None
fic_hasard = PhotoImage(file = 'Hasard.png')
b_hasard = None
fic_dahut = PhotoImage(file = 'Dahut.png')
b_dahut = None
joueur = "moi"
all_piegees = []
canv = Canvas(nim, width = 1280, height = 400, bg = "white")
canv.place(x = 50, y = 50)

def gerer_fin():
    global b_humain, b_com, b_bot
    if len(img_all) == 0:
        canv.create_text(640, 200, text = joueur + " a gagné", font = 'Arial')

def qui_joue():
    global b_humain, b_bot, b_go
    b_go.config(state = "disabled")
    if randint(0, 1) == 0:
        joueur = "moi"
        b_humain.config(state = "active")
    else :
        joueur = "machine"
        b_bot.config(state = "active")
    
def action(i):
    global joueur, b_com, b_bot
    if type_dahut:
        pieger()
    for k in range(min(i, len(img_all))):
        rang = randint(0, len(img_all) -1)
        canv.delete(img_all[rang])
        img_all.pop(rang)
    if rang in all_piegees:
        for b in b_com:
            b.config(state = "disabled")
            b_bot.config(state = "active")
            joueur = "humain"
            gerer_fin()
            
def creer_interface():
    global b_humain, b_bot, b_go, b_intelligent, b_hasard
    x = 10                  
    for i in range(0, 21):
        img1 =  canv.create_image(x, 0, image = fic_all, anchor = NW)
        img_all.append(img1)
        x += 60
    xx = 60
    for i in range(1, 4):
        b = Button(nim, image = fic_com[i - 1], command = lambda x = i: action(x),  bg = "#00F000")
        b.place(x = xx , y = 500)
        b.config(state = "disabled")
        b_com.append(b)
        xx += 60
    b_go = Button(nim, image = fic_go, command = qui_joue)
    b_go.place(x = xx, y = 500)
    b_go.config(state = "disabled")
    xx += 90
    b_humain = Button(nim, image = fic_humain, command = jouer_humain)
    b_humain.place(x = xx, y = 500)
    b_humain.config(state = "disabled")
    xx += 90
    b_bot = Button(nim, image = fic_bot, command = jouer_machine)
    b_bot.place(x = xx, y = 500)
    b_bot.config(state = "disabled")
    xx += 90
    b_intelligent = Button(nim, image = fic_intelligent, command = jeu_intel)
    b_intelligent.place(x = xx, y = 500)
    xx += 120
    b_hasard = Button(nim, image = fic_hasard, command = jouer_rnd)
    b_hasard.place(x = xx, y = 500)
    xx += 120
    b_dahut = Button(nim, image = fic_dahut, command = jeu_dahut)
    b_dahut.place(x = xx, y = 500)
    
def jeu_dahut():
    global type_dahut
    type_dahut = True
    
def pieger():
    global all_piegees
    nb_restantes = len(img_all)
    nb_piegees = round(0.15 * nb_restantes)
    tab = [i for i in range(0, nb_restantes)]
    all_piegees = tab.sample(tab, nb_piegees)
    
def jouer_rnd():
    global type_jeu_machine, b_go, b_hasard, b_intelligent
    type_jeu_machine = False
    b_go.config(state = "active")
    b_hasard.config(state = "disabled")
    b_intelligent.config(state = "disabled")

def jeu_intel():
    global type_jeu_machine
    type_jeu_machine = True
    b_go.config(state = "active")
    b_hasard.config(state = "disabled")
    b_intelligent.config(state = "disabled")
    
def jouer_humain():
    global b_com, b_humain
    b_humain.config(state = "disabled")
    for b in b_com:
        b.config(state = "active")
        
def jouer_machine():
    global b_bot, b_com, joueur
    b_bot.config(state = "disabled")
    if type_dahut:
        piegeer() 
    if not type_jeu_machine:
        i = randint(1, 3)
        for k in range(min(i, len(img_all))):
            rang = randint(0, len(img_all) -1)
            canv.delete(img_all[rang])
            img_all.pop(rang)
    else:
        nb_restantes = len(img_all)
        nb_a_jouer = nb_restantes % 4
        if nb_a_jouer == 0:
            nb_a_jouer = randint(1,  3)
        for k in range(min(nb_a_jouer, len(img_all))):
            rang = randint(0, len(img_all) -1)
            canv.delete(img_all[rang])
            img_all.pop(rang)
    b_humain.config(state = "active")
    joueur= "machine"
    gerer_fin()

def jouer():
    creer_interface()

if __name__ == "__main__":
    jouer()
    nim.mainloop() 