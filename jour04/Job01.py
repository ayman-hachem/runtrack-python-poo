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
        Personne.__init__(self, age=14)
        
    def allerEnCours(self):
        return "Je vais en cours"

    def afficherAge(self):
        return f"J'ai {self.age} ans."

class Professeur:
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def get_matiereEnseignee(self,matiereEnseignee):
        return self.__matiereEnseignee

    def set_matiereEnseignee(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee
    
    def enseignee(self):
        return "Le cours va commencer "

personne = Personne()
print(personne.afficherAge())
print(personne.bonjour())

eleve = Eleve()
print(eleve.allerEnCours())
print(eleve.afficherAge())

professeur = Professeur("math")
print(professeur.enseignee())