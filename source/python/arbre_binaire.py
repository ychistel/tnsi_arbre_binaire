class Noeud:
    
    def __init__(self, valeur=None, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit
    
    def est_vide(self):
        return self.valeur is None
    
    def __str__(self):
        if self.valeur is None:
            return ""
        else:
            return "Noeud("+str(self.valeur) + ","+ str(self.gauche) +","+ str(self.droit)+")"
    
class Arbre:
    
    def __init__(self,racine=None):
        if isinstance(racine,Noeud):
            self.racine = racine
        else:
            self.racine = Noeud(racine)
        
    def __str__(self):
        return str(self.racine)
        
    def est_vide(self):
        return self.racine.valeur is None
    
    """
    def fils_gauche(self):
        if not self.est_vide():
            return Arbre(self.racine.gauche)
        
    def fils_droit(self):
        if not self.est_vide():
            return Arbre(self.racine.droit)
    """
    
    def fils_gauche(self):
        return Arbre(self.racine.gauche)
        
    def fils_droit(self):
        return Arbre(self.racine.droit)
         
if __name__ == '__main__':
    from draw_arbre import afficher
    
    n=Noeud(7,Noeud(5,Noeud(8),Noeud(1)),Noeud(4,None,Noeud(6)))
    print(n)
    a=Arbre(n)
    print(a)
    g = afficher(a,'jpg')
    print("Pour afficher une représentation de l'arbre, saisir g.view()")
