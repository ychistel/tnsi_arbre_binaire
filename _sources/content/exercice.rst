Exercices
=========

Exercice 1
----------

.. figure:: ../img/ex_1.png
   :align: center

Les arbres 1 et 2 ci-dessus sont des arbres binaires. On suppose que la racine est de profondeur 0.

#. Donner la taille et la hauteur des arbres binaires 1 et 2.
#. Donner une construction récursive de chaque arbre.

Exercice 2
----------

Nous allons utiliser un module contenant les classes Noeud et Arbre pour construire des arbres binaires. Vous trouverez
le fichier ``arbre_binaire.py`` sur l’ENT pour l'importer en tant que module.

.. rubric:: Interface

L’interface de notre arbre binaire est la suivante.

- La méthode ``est_vide()`` renvoie un booléen : ``True`` si l'arbre est vide et ``False`` s'il n'est pas vide.
- La méthode ``fils_gauche()`` renvoie le sous arbre gauche de l'arbre.
- La méthode ``fils_droit()`` renvoie le sous arbre droit de l'arbre.
- La fonction ``print`` affiche la construction récursive de l'arbre sous forme d'une chaine de carctères.

.. rubric:: Implémentation

L'implémentation repose sur la programmation objet.

- Un objet Arbre a un attribut **racine** qui contient un objet **Noeud**.
- Un objet Noeud possède 3 attributs : valeur, gauche et droit. A la création d’un Noeud, l’attribut valeur est
  requis. Les attributs gauche et droit, s’ils ne sont pas précisés, valent None.

#. Créer trois objets de type Noeud ``a``, ``b`` et ``c`` qui ont pour valeurs respectives 4, 7 et 1.
#. Vérifier que les attributs ``gauche`` et ``droit`` du noeud ``a`` sont vides. Modifier les valeurs des attributs
   ``gauche`` et ``droit`` en leur attribuant respectivement les noeuds ``b`` et ``c``.

#. Est-ce que ``a`` est un arbre binaire ? Est-ce que ``a`` est un **objet** arbre binaire ? Si non, transformer la
   variable ``a`` en objet arbre binaire.

#. Ajouter à l'arbre binaire une feuille de valeur 6, fils gauche du noeud de valeur 7.

Exercice 3
----------

On continue avec l'implémentation POO d'un arbre binaire.

#. Créer 2 arbres binaires ``a1`` et ``a2`` représentés ci-dessous:

   .. figure:: ../img/ex_1.png
      :align: center

#. On donne l’algorithme d’une fonction pour déterminer la taille d’un arbre binaire.

   .. code-block::

      fonction taille(arbre)
         si arbre est vide:
            renvoyer 0
         sinon:
            renvoyer 1 + taille(arbre gauche) + taille(arbre droit)

   a) Quel procédé est utilisé par cette fonction pour calculer la taille d’un arbre binaire?

   b) Programmer cette fonction en python et déterminer la taille des arbres saisis à l’exercice précédent.

#. Écrire une fonction ``hauteur`` qui permet de calculer la hauteur d’un arbre binaire.

#. Créer une fonction ``niveau`` en Python qui prend un arbre et une profondeur p en paramètres et qui renvoie la liste
   des valeurs situées au niveau de profondeur p.
