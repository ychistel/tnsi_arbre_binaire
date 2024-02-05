class Noeud:
    """
    Classe implémentant un noeud d'arbre binaire disposant de 3 attributs:
    - valeur : la valeur de l'étiquette,
    - gauche : le sous-arbre gauche,
    - droit : le sous-arbre droit.
    """
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d
    
    def __str__(self):
        return "Noeud(" + str(self.gauche) + ',' + str(self.valeur) + ',' + str(self.droit) + ")"
    
    def est_une_feuille(self):
        '''Renvoie True si et seulement si le noeud est une feuille'''
        return self.gauche is None and self.droit is None


def expression_infixe(e):
    s = ...
    if e.gauche is not None:
        s = s + expression_infixe(...)
    s = s + ...
    if ... is not None:
        s = s + ...
    if ...:
        return s
    
    return '('+ s +')'
