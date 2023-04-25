class Forme:
    def aire(self):
        pass

class Cercle(Forme):
    def __init__(self, rayon):
        self.radius = rayon
    
    def aire(self):
        return 3.14 * self.radius ** 2

class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.length = longueur
        self.width = largeur
    
    def aire(self):
        return self.length * self.width

# Création d'instances
cercle1 = Cercle(5)
rectangle1 = Rectangle(10, 5)

# Tests de la méthode aire sur les instances
print("Aire du cercle : ", cercle1.aire())  # Affiche 78.5
print("Aire du rectangle : ", rectangle1.aire())  # Affiche 50
