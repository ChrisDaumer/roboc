# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""
from coordonnees import *
from obstacle import *
from robot import *
from labyrinthe import *
import os
from pickle import Pickler, Unpickler


class Carte:
    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = self.creer_labyrinthe_depuis_chaine(chaine)

    def __repr__(self):
        return "<Carte {}>".format(self.nom)

    def enregistrement_auto(self):
        chemin = os.path.join("parties", self.nom)

        with open(chemin, "wb") as file:
            file = Pickler(file)
            file.dump(self)

    def charger_partie(self):
        chemin = os.path.join("parties", self.nom)

        parties = os.listdir("parties")
        if self.nom in parties:
            with open(chemin, "rb") as file:
                file = Unpickler(file)
                return file.load()

    def creer_labyrinthe_depuis_chaine(self, chaine):
        obstacles = []
        robot = Robot(Coordonnees(-1, -1))
        x = y = 0
        longueur_ligne = chaine.find('\n')

        # Iteration sur tous les symboles de la carte (fichier)
        for num_c, c in enumerate(chaine):
            x = num_c % (longueur_ligne+1)
            if c == '\n': # saut de ligne dans la carte
                y += 1

            if c in ['O', '.', 'U']:
                obstacles.append(Obstacle(c, Coordonnees(x, y)))
            if c == 'X':
                robot = Robot(Coordonnees(x, y))

        return Labyrinthe(robot, obstacles)
