# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
from carte import *

# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-4].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            carte = Carte(nom_carte, contenu)
            cartes.append(carte)

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

# Choix d'une carte
choix = input("Entrez un numéro de labyrinthe pour commencer à jouer : ")
carte = cartes[int(choix) - 1]

# Suggestion de chargement d'une partie sauvegardee
carte_enregistre = carte.charger_partie()
if carte_enregistre is not None and carte_enregistre.labyrinthe.est_termine() is not True:
    charger_partie = input("Charger ancienne partie ? (o/n)").upper()
    if charger_partie == 'O':
        carte = carte_enregistre

labyrinthe = carte.labyrinthe

# Deplacement dans le labyrinthe
deplacement = ""
while deplacement != 'Q' and not labyrinthe.est_termine():
    print(labyrinthe)

    deplacement = input("> ").upper()
    if deplacement != '':
        direction = deplacement[0]
        if direction in ['O', 'E', 'S', 'N']:
            if len(deplacement) == 1:  # deplacement de 1 pas
                labyrinthe.deplacer(deplacement)
            elif len(deplacement) == 2 and deplacement[1].isnumeric(): # deplacement de 1 ou plusieurs pas
                labyrinthe.deplacer(deplacement[0], int(deplacement[1]))

        carte.enregistrement_auto()

if labyrinthe.est_termine():
    print("GG!")
