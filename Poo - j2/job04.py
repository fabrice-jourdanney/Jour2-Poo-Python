class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire(self):
        return self.largeur * self.hauteur

# Création d'un objet de type Rectangle
mon_rectangle = Rectangle(5, 3)

# Appel de la méthode aire de la classe Rectangle
print("L'aire du rectangle est :", mon_rectangle.aire())  # Affiche "L'aire du rectangle est : 15"
