class ABR:
    """Implémentation d'un arbre binaire de recherche (ABR)"""
    def __init__(self,valeur=None):
        self.valeur = valeur
        self.fg = None
        self.fd = None
        
    def estVide(self):
        return self.valeur == None
    
    def insererElement(self,e):
        if self.estVide()