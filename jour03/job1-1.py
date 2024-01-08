class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def get_nombre_habitants(self):
        return self.__nombre_habitants

    def set_nombre_habitants(self, nombre_habitants):
        self.__nombre_habitants = nombre_habitants

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self):
        nombre_habitants_actuel = self.__ville.get_nombre_habitants()
        self.__ville.set_nombre_habitants(nombre_habitants_actuel + 1)

# Créer un objet Ville avec comme arguments “Paris” et 1000000.
ville_paris = Ville("Paris", 1000000)
# Afficher en console le nombre d’habitants de la ville de Paris.
print(f"Nombre d'habitants de la ville de Paris : {ville_paris.get_nombre_habitants()}")

# Créer un autre objet Ville avec comme arguments “Marseille” et 861635.
ville_marseille = Ville("Marseille", 861635)
# Afficher en console le nombre d’habitants de la ville de Marseille.
print(f"Nombre d'habitants de la ville de Marseille : {ville_marseille.get_nombre_habitants()}")

# Créer les objets suivants :
# - John, 45 ans, habitant à Paris
# - Myrtille, 4 ans, habitant à Paris.
# - Chloé, 18 ans, habitant à Marseille.
john = Personne("John", 45, ville_paris)
myrtille = Personne("Myrtille", 4, ville_paris)
chloe = Personne("Chloé", 18, ville_marseille)

# Afficher le nombre d’habitants de Paris et de Marseille après l’arrivée de ces nouvelles personnes.
john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

print(f"Nombre d'habitants de la ville de Paris après l'arrivée de John et Myrtille : {ville_paris.get_nombre_habitants()}")
print(f"Nombre d'habitants de la ville de Marseille après l'arrivée de Chloé : {ville_marseille.get_nombre_habitants()}")
