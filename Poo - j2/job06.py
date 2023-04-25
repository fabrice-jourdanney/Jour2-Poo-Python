class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix
        
    def informationsVehicule(self):
        print(f"Marque : {self.marque}\nAnnée : {self.annee}\nPrix : {self.prix}")
        
    def demarrer(self):
        print("Attention, je roule.")

class Voiture(Vehicule):
    def __init__(self, marque, annee, prix):
        super().__init__(marque, annee, prix)
        self.portes = 4
        
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Portes : {self.portes}")

    def demarrer(self):
        print(f"La voiture {self.marque} démarre.")
        
class Moto(Vehicule):
    def __init__(self, marque, annee, prix):
        super().__init__(marque, annee, prix)
        self.roue = 2
        
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Roues : {self.roue}")

    def demarrer(self):
        print(f"La moto {self.marque} démarre.")

#instanciation de la voiture
ma_voiture = Voiture("Peugeot", 2019, 18000)
ma_voiture.informationsVehicule()
ma_voiture.demarrer()

#instanciation de la moto
ma_moto = Moto("Yamaha", 2021, 9000)
ma_moto.informationsVehicule()
ma_moto.demarrer()
