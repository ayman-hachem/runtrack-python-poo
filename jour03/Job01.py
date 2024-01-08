class Ville:
    def __init__(self, nom: str, nombre_habitant: int):
        self.__nom = nom
        self.__nombre_habitant = nombre_habitant

    def get_habitant(self):
        return self.__nombre_habitant 

    def get_nom(self):
        return self.__nom

    def set_habitant(self, nombre_habitant):
        self.__nombre_habitant = nombre_habitant

    def set_nom(self, nom):
        self.__nom = nom

    def afficher_nb_habitant(self):
        return f"La ville de {self.get_nom()} a {self.get_habitant()} habitants"


marseille = Ville("Marseille", 1000000)
# Afficher le nombre d’habitants de la ville de Marseille.
print(marseille.afficher_nb_habitant())

paris = Ville("Paris", 861635)
# Afficher le nombre d’habitants de la ville de Paris.
print(paris.afficher_nb_habitant())


class Personne:
    def __init__(self, prenom: str, age: int, ville: Ville):
        self.__prenom = prenom
        self.__age = age
        self.__ville = ville

    def get_prenom(self):
        return self.__prenom
    
    def get_age(self):
        return self.__age
    
    def get_ville(self):
        return self.__ville
    
    def set_prenom(self, prenom):
        self.__prenom = prenom
      
    def set_age(self, age):
        self.__age = age
        
    def ajouterPopulation(self):
        nombre_habitants_actuel = self.__ville.get_habitant()
        self.__ville.set_habitant(nombre_habitants_actuel + 1)
        

john = Personne("John", 49, paris)# - John, 49 ans, habitant à Paris
myrtille = Personne("Myrtille", 4, marseille)# - Myrtille, 4 ans, habitant à Marseille
chloe = Personne("Chloé", 13, paris)# - Chloé, 13 ans, habitant à Paris

# Afficher le nombre d’habitants de Paris et de Marseille après l’arrivée de ces nouvelles personnes.
john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

print(paris.afficher_nb_habitant())
print(marseille.afficher_nb_habitant())


