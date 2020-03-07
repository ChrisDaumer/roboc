# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""
from coordonnees import *

class Labyrinthe:
    """Classe représentant un labyrinthe."""

    def __init__(self, robot, obstacles):
        self.robot = robot
        self.grille = {}

        for obstacle in obstacles:
            # Placement des obstacles dans un dict
            # Chaque obstacle est place selon ses cooordonnees
            self.grille[obstacle.coordonnees.x, obstacle.coordonnees.y] = obstacle.nature

    def deplacer(self, direction, distance=1):
        prochaine_position = Coordonnees(self.robot.coordonnees.x, self.robot.coordonnees.y)

        for i in range(distance):

            if direction == 'O':
                prochaine_position.x, prochaine_position.y = self.robot.coordonnees.x - 1, self.robot.coordonnees.y
            elif direction == 'E':
                prochaine_position.x, prochaine_position.y = self.robot.coordonnees.x + 1, self.robot.coordonnees.y
            elif direction == 'N':
                prochaine_position.x, prochaine_position.y = self.robot.coordonnees.x, self.robot.coordonnees.y - 1
            elif direction == 'S':
                prochaine_position.x, prochaine_position.y = self.robot.coordonnees.x, self.robot.coordonnees.y + 1

            if (prochaine_position.x, prochaine_position.y) in self.grille:  # si prochaine position robot = obstacle ou sortie
                if self.grille[(prochaine_position.x, prochaine_position.y)] == 'O':
                    break
                if self.grille[(prochaine_position.x, prochaine_position.y)] == 'U':
                    self.robot.coordonnees = Coordonnees(prochaine_position.x, prochaine_position.y)
                    break

            self.robot.coordonnees = Coordonnees(prochaine_position.x, prochaine_position.y)

    def est_termine(self):
        if (self.robot.coordonnees.x, self.robot.coordonnees.y) in self.grille:
            if self.grille[(self.robot.coordonnees.x, self.robot.coordonnees.y)] == 'U':
                return True

    def __str__(self):
        chaine = ""
        longueur_ligne = 0
        nombre_ligne = 0

        # position[0] : x
        # position[1] : y
        # Recherche de la longueur (x) et hauteur (y) maximum
        for position in self.grille:
            if position[0] > longueur_ligne:
                longueur_ligne = position[0]
            if position[1] > nombre_ligne:
                nombre_ligne = position[1]

        # Ajoute dans une chaine les caracteres ligne par ligne
        for y in range(nombre_ligne + 1):
            for x in range(longueur_ligne + 1):
                if (x, y) == (self.robot.coordonnees.x, self.robot.coordonnees.y):
                    chaine += 'X'
                elif (x, y) in self.grille:
                    chaine += self.grille[(x, y)]
                else:
                    chaine += ' '
            chaine += '\n'

        return chaine
