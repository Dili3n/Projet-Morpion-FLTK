# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:22:27 2020

@author: Dilien
"""

"""
Comment jouer ? 
Le morpion est un jeu de plateau qui se joue à deux ! 
Le but est de former une ligne de 3 formes (cercle ou croix)
Pour cela le joueur 1 controle les croix avec le clic gauche
de la souris et le joueur 2 les cercles avec le clic droit.
Il faut jouer chacun son tour ! 
Si vous vous trompez vous pouvez quitter une partie pendant
celle-ci ! A vous de jouer !
"""



from fltk import *
from time import sleep
from random import *

score1 = 0
score2 = 0

boucle = True

menu = True
morpion = False
win = False

winj1 = False
winj2 = False
egalite = False

largeur_plateau = 600  # en nombre de cases
hauteur_plateau = 620  # en nombre de cases

cree_fenetre(largeur_plateau, hauteur_plateau)

def winner(grille):
    casvictoire = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[1, 5, 9],[3, 5, 7],[1, 4, 7],[2, 5, 8],[3, 6, 9]]
        
    if (grille[0] == grille[1]) and (grille[0] == grille[2]):
        if grille[0] == [1]:
            return 1
        elif grille[0] == [2]:
            return 2
    if (grille[3] == grille[4]) and (grille[3]==grille[5]):
        if grille[3] == [1]:
            return 1
        elif grille[3] == [2]:
            return 2
    if (grille[6] == grille[7]) and (grille[6] == grille[8]):
        if grille[6] == [1]:
            return 1
        elif grille[6] == [2]:
            return 2
    if (grille[0] == grille[3]) and (grille[0] == grille[6]):
        if grille[0] == [1]:
            return 1
        elif grille[0] == [2]: 
            return 2
    if (grille[1] == grille[4]) and (grille[1] == grille[7]):
        if grille[1] == [1]:
            return 1
        elif grille[1] == [2]: 
            return 2
    if (grille[2] == grille[5]) and (grille[2] == grille[8]):
        if grille[2] == [1]:
            return 1
        elif grille[2] == [2]: 
            return 2
    if (grille[0] == grille[4]) and (grille[0] == grille[8]):
        if grille[0] == [1]:
            return 1
        elif grille[0] == [2]:
            return 2
    if (grille[2] == grille[4]) and (grille[2] == grille[6]):
        if grille[2] == [1]:
            return 1
        elif grille[2] == [2]:
            return 2

while boucle:
    
    rectangle(0,0,600,620,epaisseur=3)
    
    mise_a_jour()
    
    case1 = False
    case2 = False
    case3 = False
    case4 = False
    case5 = False
    case6 = False
    case7 = False
    case8 = False
    case9 = False
    
    total_grille = 0
    
    grille = [0,0,0
             ,0,0,0
             ,0,0,0]
    
    while menu:
        
        rectangle(0,0,600,620,epaisseur=3)
        rectangle(0,0,600,600,epaisseur=3)
        
        image(300,300,'assets/bgmenu.png', ancrage = "center")
        
        texte(10,604,("Score1",score1), couleur = 'black',police = 'benguiat',
              taille ='10')
        
        texte(520,604,("Score2",score2), couleur = 'black',police = 'benguiat',
              taille ='10')
        
        texte(250,410,"Jouer", couleur = 'darkblue',police = 'benguiat')
    
        # gestion des événements
        ev = donne_ev()
        ty = type_ev(ev)
        
        # Quand on quitte le jeu il se ferme, et ne crash pas
        if ty == 'Quitte':
            menu = False
            boucle = False
            break
        
        elif ty == "ClicGauche":
            if 200 <= abscisse(ev) <= 400 and 400 <= ordonnee(ev) <= 450:
                texte(250,410,"Jouer", couleur = 'darkred',police = 'benguiat')
                mise_a_jour()
                sleep(0.5)
                menu = False
                morpion = True
    
    
        mise_a_jour()
    
        efface_tout()
    
    if morpion:
        image(300,300,'assets/bgjeu.png', ancrage = "center")
        
    while morpion:
        
        texte(280,604,"Quitter", couleur = 'black',police = 'benguiat',
              taille ='10')
        
        texte(10,604,("Score1",score1), couleur = 'black',police = 'benguiat',
              taille ='10')
        
        texte(520,604,("Score2",score2), couleur = 'black',police = 'benguiat',
              taille ='10')
        
        rectangle(0,0,600,600,epaisseur=3)
        rectangle(0,0,600,620,epaisseur=3)
        
        ligne(200,0,200,600)
        ligne(400,0,400,600)
        ligne(0,200,600,200)
        ligne(0,400,600,400)
        
        # gestion des événements
        ev = donne_ev()
        ty = type_ev(ev)
        
        # Quand on quitte le jeu il se ferme, et ne crash pas
        if ty == 'Quitte':
            morpion = False
            boucle = False
            break
        elif ty == "ClicGauche":
            
            if 0 <= abscisse(ev) <= 200 and 0 <= ordonnee(ev) <= 200 and case1 == False:
                ligne(0,0,200,200)
                ligne(200,0,0,200)
                grille[0] = [1]
                total_grille  += 1
                case1 = True
            elif 200 <= abscisse(ev) <= 400 and 0 <= ordonnee(ev) <= 200 and case2 == False:
                ligne(200,0,400,200)
                ligne(400,0,200,200)
                grille[1] = [1]
                total_grille  += 1
                case2 = True
            elif 400 <= abscisse(ev) <= 600 and 0 <= ordonnee(ev) <= 200 and case3 == False:
                ligne(400,0,600,200)
                ligne(600,0,400,200)
                grille[2] = [1]
                total_grille  += 1
                case3 = True
            elif 0 <= abscisse(ev) <= 200 and 200 <= ordonnee(ev) <= 400 and case4 == False:
                ligne(0,200,200,400)
                ligne(200,200,0,400)
                grille[3] = [1]
                total_grille  += 1
                case4 = True
            elif 200 <= abscisse(ev) <= 400 and 200 <= ordonnee(ev) <= 400 and case5 == False:
                ligne(200,200,400,400)
                ligne(200,400,400,200)
                grille[4] = [1]
                total_grille  += 1
                case5 = True
            elif 400 <= abscisse(ev) <= 600 and 200 <= ordonnee(ev) <= 400 and case6 == False:
                ligne(400,200,600,400)
                ligne(600,200,400,400)
                grille[5] = [1]
                total_grille  += 1
                case6 = True
            elif 0 <= abscisse(ev) <= 200 and 400 <= ordonnee(ev) <= 600 and case7 == False:
                ligne(0,400,200,600)
                ligne(200,400,0,600)
                grille[6] = [1]
                total_grille  += 1
                case7 = True
            elif 200 <= abscisse(ev) <= 400 and 400 <= ordonnee(ev) <= 600 and case8 == False:
                ligne(200,400,400,600)
                ligne(200,600,400,400)
                grille[7] = [1]
                total_grille  += 1
                case8 = True
            elif 400 <= abscisse(ev) <= 600 and 400 <= ordonnee(ev) <= 600 and case9 == False:
                ligne(400,400,600,600)
                ligne(600,400,400,600)
                grille[8] = [1]
                total_grille  += 1
                case9 = True
            elif 260 <= abscisse(ev) <= 360 and 601 <= ordonnee(ev) <= 620:
                morpion = False
                menu = True
                
        elif ty == "ClicDroit":
            
            if 0 <= abscisse(ev) <= 200 and 0 <= ordonnee(ev) <= 200 and case1 == False:
                cercle(100,100,100)
                case1 = True
                total_grille  += 1
                grille[0] = [2]
            elif 200 <= abscisse(ev) <= 400 and 0 <= ordonnee(ev) <= 200 and case2 == False:
                cercle(300,100,100)
                case2 = True
                total_grille  += 1
                grille[1] = [2]
            elif 400 <= abscisse(ev) <= 600 and 0 <= ordonnee(ev) <= 200 and case3 == False:
                cercle(500,100,100)
                case3 = True
                total_grille  += 1
                grille[2] = [2]
            elif 0 <= abscisse(ev) <= 200 and 200 <= ordonnee(ev) <= 400 and case4 == False:
                cercle(100,300,100)
                case4 = True
                total_grille  += 1
                grille[3] = [2]
            elif 200 <= abscisse(ev) <= 400 and 200 <= ordonnee(ev) <= 400 and case5 == False:
                cercle(300,300,100)
                case5 = True
                total_grille  += 1
                grille[4] = [2]
            elif 400 <= abscisse(ev) <= 600 and 200 <= ordonnee(ev) <= 400 and case6 == False:
                cercle(500,300,100)
                case6 = True
                total_grille  += 1
                grille[5] = [2]
            elif 0 <= abscisse(ev) <= 200 and 400 <= ordonnee(ev) <= 600 and case7 == False:
                cercle(100,500,100)
                case7 = True
                total_grille  += 1
                grille[6] = [2]
            elif 200 <= abscisse(ev) <= 400 and 400 <= ordonnee(ev) <= 600 and case8 == False:
                cercle(300,500,100)
                case8 = True
                total_grille  += 1
                grille[7] = [2]
            elif 400 <= abscisse(ev) <= 600 and 400 <= ordonnee(ev) <= 600 and case9 == False:
                cercle(500,500,100)
                case9 = True
                total_grille  += 1
                grille[8] = [2]
                
        mise_a_jour()
    
        gagnant = winner(grille)
            
        if gagnant == 1:
            morpion = False
            winj1 = True
            win = True
            score1 += 1
        elif gagnant == 2:
            morpion = False
            winj2 = True
            win = True
            score2 += 1
        elif total_grille == 9:
            win = True
            egalite = True
            morpion = False
        
    while win:
        
        efface_tout()
        
        rectangle(0,0,600,600,epaisseur=3)
        rectangle(0,0,600,620,epaisseur=3)
        
        texte(10,604,("Score1",score1), couleur = 'black',police = 'benguiat',
              taille ='10')
        
        texte(520,604,("Score2",score2), couleur = 'black',police = 'benguiat',
              taille ='10')
        
        if winj1:
            image(300,300,'assets/bgwinj1.png', ancrage = "center")
        elif winj2:
            image(300,300,'assets/bgwinj2.png', ancrage = "center")
        elif egalite:
            image(300,300,'assets/bgegalite.png', ancrage = "center")
            
        texte(0,0,("by Dilien"), couleur = 'blue',taille ='6')
        texte(80,510,"Rejouer", couleur = 'darkblue',police = 'benguiat')
        texte(400,510,"Menu", couleur = 'darkblue',police = 'benguiat')
        
        mise_a_jour()
        
        # gestion des événements
        ev = donne_ev()
        ty = type_ev(ev)
        
        if ty == 'Quitte':
            win = False
            boucle = False
            break
        
        if ty == "ClicGauche":
            if 50 <= abscisse(ev) <= 250 and 500 <= ordonnee(ev) <= 550:
                texte(80,510,"Rejouer", couleur = 'darkred',police = 'benguiat')
                mise_a_jour()
                sleep(0.5)
                morpion = True
                winj1 = False
                winj2 = False
                egalite = False
                win = False
                
            elif 350 <= abscisse(ev) <= 550 and 500 <= ordonnee(ev) <= 550:
                texte(400,510,"Menu", couleur = 'darkred',police = 'benguiat')
                mise_a_jour()
                sleep(0.5)
                winj1 = False
                winj2 = False
                egalite = False
                menu = True
                win = False
        
        efface_tout()
    
ferme_fenetre()