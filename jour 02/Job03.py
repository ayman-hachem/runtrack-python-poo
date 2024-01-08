class Livre:
    def __init__(self, titre, auteur, nombre_pages: int, disponible = True):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
        self.__disponible = disponible
        
        
    def get_titre(self):
        return self.__titre()
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nombre_pages(self):
        return self.__nombre_pages
    
    def get_disponible(self):
        return self.__disponible
    
 
    def set_nombre_page(self, nombre_pages) :
        self.__nombre_pages = nombre_pages
        if nombre_pages < 0 :
            return "Erreur : Le nombre de pages doit être un entier positif. "
        else:
            return f"Le livre à {nombre_pages} pages."
    
    def verification(self):
        return self.__disponible
          
     
        
    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
            return "le livre est maintenant emprunter"
        else:
            return "Le live n'est plus disponible"


    def rendre(self):
        if not self.verification():
            self.__disponible = True
            return "Le livre a été rendu avec succès."
        else:
            return "Le livre n'est pas encore rendu."

       
       
       
livre = Livre("x", "xxx", 0, True)
print(livre.set_nombre_page(25))
print(livre.verification())
print(livre.emprunter())
print(livre.verification())
    