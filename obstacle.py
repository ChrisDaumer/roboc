class Obstacle:

    def __init__(self, nature, coordonnees):
        self.nature = nature
        self.coordonnees = coordonnees

    def __str__(self):
        return "Obstacle:{}[{}, {}]".format(self.nature, self.coordonnees)
