
class Comptebancaire:
    def __init__(self, num_compte, prenom, nom, solde, decouvert: bool):
        self.__num_compte = num_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert
    def get_num_compte(self):
        return self.__num_compte
    
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def get_solde(self):
        return self.__solde
    
    def get_decouvert(self):
        return self.__decouvert
    
    def set_solde(self, solde):
        self.__solde = solde
       
    def set_nom(self, nom):
        self.__nom = nom 
    
    def set_prenom(self, prenom):
        self.__prenom = prenom
    
    def set_decouvert(self, decouvert):
        self.__decouvert = decouvert
    
    def afficher_client(self):
        return f'le client est {self.get_prenom()} {self.get_nom()}, {self.get_num_compte()}, {self.get_solde()} €'

    def afficher_solde(self):
        return f'{self.get_prenom()} {self.get_nom()} votre solde est de {self.get_solde()} €'
    
    def versement(self, montant):
    
        if montant > 0:
            self.__solde += montant
            return f"Versement de {montant} € effectué."
            
        else:
            return f"Erreur : Le montant du versement doit être positif."
            
    def retrait(self, montant):
        if montant > 0 and montant <= self.__solde:
            self.__solde -= montant
            return f"Retrait de {montant} € effectué."
            
        else:
            return f"Erreur : Montant invalide ou solde insuffisant pour effectuer le retrait.."
        
    def decouvert(self, decouvert):
        if self.get_solde() <= 0 and decouvert == True:
            self.__decouvert = abs(self.get_solde()) * 0.5
            print("Découvert autorisé. Montant du découvert:", self.__decouvert)
        else:
            print("Découvert non applicable.")
            
    def virement(self, compte_destinataire, montant):
        if montant > 0 and montant <= self.__solde:
            self.__solde -= montant
            compte_destinataire.__solde += montant
            return f"Virement de {montant} € effectué vers le compte de {compte_destinataire.get_prenom()} {compte_destinataire.get_nom()}."
        else:
            return f"Erreur : Montant invalide ou solde insuffisant pour effectuer le virement."

personne1 = Comptebancaire(15658987450, "Jean", "Aimarre", 550, True)
personne2 = Comptebancaire(1252585228, "Touc", "Asser", -300,False)

print(personne1.afficher_solde())
print(personne1.afficher_client())
print(personne2.afficher_solde())
print(personne2.afficher_client())
print(personne1.versement(50))
print(personne1.afficher_solde())
print(personne1.retrait(1))
print(personne1.afficher_solde())

print(personne1.virement(personne2, 400))
print(personne1.afficher_solde())
print(personne2.afficher_solde())
