class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def bonjour(self):
        print(f"Bonjour, je m'appelle {self.nom}.")

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours.")

eleve = Eleve("Jean", 15)
eleve.bonjour()
eleve.allerEnCours()
eleve.age = 15

class Professeur(Personne):
    def enseigner(self):
        print("Le cours commence.")

prof = Professeur("Marie", 40)
prof.bonjour()
prof.enseigner()

