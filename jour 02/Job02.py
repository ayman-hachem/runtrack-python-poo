class Livre:
    def __init__(self, titre, auteur, nombre_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
        
    def get_titre(self):
        return self.__titre()
    
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nombre_pagesc(self):
        return self.__nombre_pages
    
    def set_nombre_page(self, nombre_pages) :
        self.__nombre_pages = nombre_pages
        if nombre_pages < 0 :
            return "Erreur : Le nombre de pages doit être un entier positif. "
        else:
            return f"Le livre a maintenant {nombre_pages} pages."
            
            
livre = Livre( "prout", "menbas",10)
print(livre.set_nombre_page(25))
    