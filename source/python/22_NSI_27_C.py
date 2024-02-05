a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], \
     'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}


def taille(arbre,nd):
    # c'est une feuille, on ajoute 1 à la taille
    if arbre[nd][0] == '' and arbre[nd][1] == '':
        return 1
    # il y a uniquement un sous arbre gauche
    elif arbre[nd][0] != '' and arbre[nd][1] == '':
        return 1+taille(arbre,arbre[nd][0])
    # il y a uniquement un sous arbre droit
    elif arbre[nd][1] != '' and arbre[nd][0] == '':
        return 1+taille(arbre,arbre[nd][1])
    # il y a deux sous arbre gauche et droit
    else:
        return 1 + taille(arbre,arbre[nd][0]) + taille(arbre,arbre[nd][1])
    
t = taille(a,'F')
    
"""
def tri_iteratif(tab):
    for k in range( ... , 0, -1):
        imax = ...
        for i in range(0 , ... ):
            if tab[i] > ... :
                imax = i
        if tab[imax] > ... :
            ... , tab[imax] = tab[imax] , ...
    return tab
"""