class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        
    def get_longueur(self):  # get recuperer et afficher  la valeur
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def affichage(self):
        return f"la longeur est {self.get_longueur()} et la largeur est {self.get_largeur()}"
    
    def set_longueur(self, longueur):  #set =  modifier une valeur
        self.__longueur = longueur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur
    
        
mon_rectangle = Rectangle(10, 5) 
       
print(mon_rectangle.affichage())
mon_rectangle.set_longueur(99999)
mon_rectangle.set_largeur(68)
print(mon_rectangle.affichage())


    
  