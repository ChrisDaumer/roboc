class Robot:

    def __init__(self, coordonnees):
        self.coordonnees = coordonnees

    def __str__(self):
        return "Robot:{}".format(self.coordonnees)
