.. TNSI

Logarithme en base 2
--------------------

Le **logarithme en base 2** d’un nombre entier :math:`n` est le nombre :math:`k` tel que l’on a :math:`2^{k} = n`.

On note :math:`k=\log_{2}(n)`. Pour tout nombre entier positif :math:`k` : :math:`\log_{2}(2^{k}) = k`

.. container::
   :name: exemple

   .. rubric:: Exemple
      :name: exemple

-  :math:`\log_{2}(8) = \log_{2}(2^{3}) = 3`

-  :math:`\log_{2}(16) = \log_{2}(2^{4}) = 4`

-  | Qu’en est-il d’un nombre strictement compris entre 8 et 16 ?
   | par exemple : :math:`\log_{2}(10) \approx 3,322` mais avec cette
     valeur approchée on a :math:`2^{3,322} \approx 10,0005`.

.. container::
   :name: propriuxe9tuxe9

   .. rubric:: Propriété
      :name: propriuxe9tuxe9

Le logarithme en base 2 d’un entier :math:`n` est compris entre les
valeurs entières :math:`p` et :math:`p-1` où :math:`p` est le nombre
minimal de bits nécessaires à l’écriture binaire du nombre :math:`n`.

.. container::
   :name: exemple-1

   .. rubric:: Exemple
      :name: exemple-1

Logarithme en base 2 de l’entier :math:`47` :
:math:`\log_{2}(47) \approx 5,55`

**Méthode mathématique:**

Comme :math:`2^{5}=32` et :math:`2^{6}=64` donc :

.. math:: 2^{5} < 47 < 2^{6} \Longleftrightarrow \log_{2}(2^{5}) < \log_{2}(47) < \log_{2}(2^{6}) \Longleftrightarrow 5 < \log_{2}(47) < 6

**Méthode informatique:**

Le nombre :math:`47` s’écrit en binaire :math:`101111_{2}`.

Il faut :math:`p=6` bits au minimum pour l’écrire en binaire, donc :

.. math:: 6-1 \leqslant \log_{2}(47) \leqslant 6 \Longleftrightarrow 5 < \log_{2}(47) < 6
