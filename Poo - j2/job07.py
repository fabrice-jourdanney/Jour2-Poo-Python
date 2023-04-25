import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = []
        couleurs = ['Pique', 'Coeur', 'Trèfle', 'Carreau']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        for couleur in couleurs:
            for valeur in valeurs:
                carte = Carte(valeur, couleur)
                self.paquet.append(carte)

    def melanger(self):
        random.shuffle(self.paquet)

    def tirer_carte(self):
        return self.paquet.pop()

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []
        self.total = 0

    def ajouter_carte(self, carte):
        self.main.append(carte)
        if carte.valeur == 'As':
            if self.total + 11 > 21:
                self.total += 1
            else:
                self.total += 11
        elif carte.valeur in ['Valet', 'Dame', 'Roi']:
            self.total += 10
        else:
            self.total += int(carte.valeur)

    def afficher_main(self):
        print(f"Main de {self.nom}:")
        for carte in self.main:
            print(f"{carte.valeur} de {carte.couleur}")
        print(f"Total: {self.total}")

class Blackjack:
    def __init__(self):
        self.jeu = Jeu()
        self.jeu.melanger()
        self.joueur = Joueur("Joueur")
        self.croupier = Joueur("Croupier")

    def jouer(self):
        # Le joueur et le croupier reçoivent chacun deux cartes
        for i in range(2):
            self.joueur.ajouter_carte(self.jeu.tirer_carte())
            self.croupier.ajouter_carte(self.jeu.tirer_carte())

        # Affichage de la main du joueur
        self.joueur.afficher_main()

        # Le joueur prend des cartes supplémentaires
        while True:
            choix = input("Voulez-vous tirer une carte ? (o/n) ")
            if choix.lower() == 'o':
                self.joueur.ajouter_carte(self.jeu.tirer_carte())
                self.joueur.afficher_main()
                if self.joueur.total > 21:
                    print("Vous avez dépassé 21, vous avez perdu.")
                    return
            else:
                break

        # Le croupier tire des cartes jusqu'à avoir un total d'au moins 17
        while self.croupier.total < 17:
            self.croupier.ajouter_carte(self.jeu.tirer_carte())

        # Affichage de la main du croupier
        self.croupier.afficher_main()

        # Détermination du vainqueur
        if self.joueur.total > 21:
            print("Vous avez dépassé 21, vous avez perdu.")
        elif self.croupier.total > 21:
            print("Le croupier a dépassé 21, vous avez gagné !")
