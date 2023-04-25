class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvelAge):
        self.age = nouvelAge

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        super().__init__()
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

    def getMatiereEnseignee(self):
        return self.__matiereEnseignee
p = Personne()
p.afficherAge()  # affiche "J'ai 14 ans"
p.bonjour()  # affiche "Hello"
p.modifierAge(25)
p.afficherAge()  # affiche "J'ai 25 ans"

e = Eleve()
e.affichageAge()  # affiche "J'ai 14 ans"
e.allerEnCours()  # affiche "Je vais en cours"

prof = Professeur("maths")
prof.enseigner()  # affiche "Le cours va commencer"
print(prof.getMatiereEnseignee())  # affiche "maths"
