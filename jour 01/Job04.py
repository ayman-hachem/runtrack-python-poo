class Operation:
    def __init__(self, prenom: str, nom: str):
        self.nom = nom
        self.prenom = prenom
   
    def personne(self):
         return "Je suis " + self.nom + " " + self.prenom
operation = Operation("John", "Doe")
operation2 = Operation("Dupond", "Jean")

print(operation.personne())
print(operation2.personne())
