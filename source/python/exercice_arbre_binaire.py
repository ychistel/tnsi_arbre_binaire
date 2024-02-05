from arbre_binaire import *
from draw_arbre import afficher

n=Noeud(7,Noeud(5,Noeud(8),Noeud(1)),Noeud(4,None,Noeud(6)))
a=Arbre(n)

g = afficher(a,'jpg')

print("Pour afficher une représentation de l'arbre, saisir g.view()")


def taille_arbre(a):
    """
    fonction récursive qui renvoie la taille d'un arbre
    paramètre:
    - a : objet arbre binaire
    retour:
    - taille de l'arbre
    """
    if a.est_vide():
        return 0
    else:
        return 1 + taille_arbre(a.fils_gauche()) + taille_arbre(a.fils_droit())

def hauteur_arbre(a):
    """
    fonction récursive qui renvoie la hauteur d'un arbre.
    la racine de l'arbre a une hauteur de 0.
    paramètre:
    - a : objet arbre binaire
    retour:
    - hauteur de l'arbre
    """
    if a.est_vide():
        return -1
    else:
        return 1 + max(hauteur_arbre(a.fils_gauche()),hauteur_arbre(a.fils_droit()))

def niveau_arbre(a,p,nds=[]):
    """
    fonction récursive qui renvoie les valeurs des noeuds de même profondeur d'un arbre
    paramètre:
    - a : objet arbre binaire
    - p : profondeur souhaitée
    - nds : liste des noeuds de même niveau
    retour:
    - nds qui contient les noeuds de profondeur p
    """
    if p <= hauteur_arbre(a):
        if p == 0:
            if not a.est_vide():
                # on empile dans une liste les valeurs
                nds.append(a.racine.valeur)
        else:
            niveau_arbre(a.fils_gauche(),p-1,nds)
            niveau_arbre(a.fils_droit(),p-1,nds)
        return nds
    else:
        return []

print("Taille de l'arbre:",taille_arbre(a))
print("Hauteur de l'arbre:",hauteur_arbre(a))
for i in range(hauteur_arbre(a)+2):
    print("Niveau %s : %s" % (i,niveau_arbre(a,i,[])))


