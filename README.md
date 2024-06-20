Fichier README
===================

Introduction
------------

L'objectif de cette librairie est de créer un générateur d'image des ensembles fractal de Mandelbrot et de Julia. Ce premier ensemble se définit comme l'ensemble des complexes c tels que la suite $ z_{n+1} = z_{n}^{2} + c $ est bornée, avec $ z_{0} = 0 $. Le second se définit avec la même suite mais $ z_{0} $ est différent de 0. Ainsi, l’ensemble de Julia pour un c complexe fixé est constitué de l’ensemble des $z_{0}$ complexes pour lesquels $ z_{n+1} = z_{n}^{2}+c $ converge.

Fonctionnement 
------------

Pour visualiser des images de fractales, il faut faire appel à plot_mandelbrot et plot_julia en spécifiant la zone du plan complexe qui nous intéresse, la valeur de z0 pour julia, de c, la précision souhaitée (via le nombre max d'itérations), la taille de pixels souhaitée et le nom de l'image à enregistrer. 
Ces deux fonctions determinent grâce à is_in_julia ou is_in_mandelbrot si les points considérés, dans la zone du plan complexe choisie, appartiennent aux ensembles ou non.
Pour chaque point, on calcule les max_iter premiers termes de la suite et on verifie que tous les termes sont dans le cercle de rayon 2 du plan complexe. Si oui, le point est noir, sinon il est blanc. 
Pour generer les suites de julia et de mandelbrot, on a crée les générateurs suite_mandelbrot et suite_julia

Aide
------------

- Le projet a été créé sous python 3.11.
- Les librairies utilisées sont numpy et matplolib
- Pour modifier le chemin de sauvegarde des images, il faut modifier l'argument du plt.savefig à la dernière ligne des fonctions plot_mandelbrot (ligne 158) et plot_julia (ligne 201)
- Les fonctions plot_lucia et plot_mandelbrot sont dans : mon_module/tp_final.py
