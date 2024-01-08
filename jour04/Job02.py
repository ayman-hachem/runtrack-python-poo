class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        return f"L'âge de la personne est {self.age} ans."

    def bonjour(self):
        return "Hello"

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age

class Eleve(Personne):
    def __init__(self):
        super().__init__(age=14)
        
    def allerEnCours(self):
        return "Je vais en cours"

    def afficherAge(self):
        return f"J'ai {self.age} ans."
    
    def modifierAge(self, nouvel_age):
        super().modifierAge(nouvel_age)

class Professeur(Personne):
    def __init__(self, matiere_enseignee, age=40):
        super().__init__(age)
        self.__matiere_enseignee = matiere_enseignee

    def get_matiere_enseignee(self):
        return self.__matiere_enseignee

    def set_matiere_enseignee(self, matiere_enseignee):
        self.__matiere_enseignee = matiere_enseignee
    
    def enseigner(self):
        return "Le cours va commencer"

# Example usage:
personne = Personne()
print(personne.afficherAge())
print(personne.bonjour())

eleve = Eleve()
print(eleve.allerEnCours())
print(eleve.afficherAge(15))


personne = Personne()
print(personne.afficherAge())
print(personne.bonjour())

eleve = Eleve()
print(eleve.allerEnCours())
print(eleve.afficherAge())
print(eleve.modifierAge(15))

professeur = Professeur("math")
print(professeur.enseignee())