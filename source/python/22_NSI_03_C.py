# --------------------
# EXERCICE 1
# --------------------

"""
def delta(t):
    d = [t[0]]
    for i in range(1,len(t)):
        d.append(t[i]-t[i-1])
    return d
"""

def delta(t):
    return [t[0]]+[t[i]-t[i-1] for i in range(1,len(t))]

assert delta([1000,800,802,1000,1003]) == [1000, -200, 2, 198, 3]
assert delta([42]) == [42]

# --------------------
# EXERCICE 2
# --------------------

class Noeud:
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d
    
    def __str__(self):
        return str(self.valeur)
    
    def est_une_feuille(self):
        '''Renvoie True si et seulement si le noeud est une feuille'''
        return self.gauche is None and self.droit is None


def expression_infixe(e):
    s = ''
    if e.gauche is not None:
        s = s + expression_infixe(e.gauche)
    s = s + str(e.valeur)
    if e.droit is not None:
        s = s + expression_infixe(e.droit)
    if e.est_une_feuille():
        return s
    
    return '('+ s +')'

e = Noeud(Noeud(Noeud(None,3,None),'*', Noeud(Noeud(None,8,None),
    '+', Noeud(None,7,None))),'-',Noeud(Noeud(None, 2, None),'+',Noeud(None,1,None)))
print(expression_infixe(e))

