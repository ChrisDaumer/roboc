class Coordonnees:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_coordonnees(self):
        return self.x, self.y

    def __str__(self):
        return "[{}:{}]".format(self.x, self.y)

    def __repr__(self):
        return str(self)