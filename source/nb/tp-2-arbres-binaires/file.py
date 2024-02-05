"""
Module : implémentation d'une File par des listes chainées en POO
Objets
- Cellule : permet de construire chaque élément de la File
- File : permet de construire une liste chainée créant une file.
Fonctions
- creer_file : pour construire une file vide.
"""

class Cellule:
    """
    type : objet
    attributs : 
    - valeur : contient la valeur passée en argument, None par défaut si pas de valeur
    - suivant : None par défaut ou un objet Cellule pour construire une liste chainée.
    méthodes:
    - constructeur : __init__
    - est_vide : renvoie un booléen (False, True) si la cellule est vide ou non
    - __repr__ : affiche la Cellule sous la forme (valeur, suivant)
    """
    def __init__(self,v=None,s=None):
        self.valeur=v
        self.suivant=s
        
    def est_vide(self):
        return self.suivant==None
    
    def __repr__(self):
        if self.valeur is None:
            return str(self.valeur)
        else:
            return "("+str(self.valeur)+","+str(self.suivant)+")"

class File:
    """
    type : objet de type liste chainée
    attributs :
    - queu