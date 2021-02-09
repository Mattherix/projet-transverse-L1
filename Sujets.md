# Cahier des charges

Matthieu ROQUEJOFFRE (chef d'équipe)

Médéric ZHOU SUN
Alexis UNG
Soanja RAVALISAONA
Anais HAMADA

## Propositions de sujets pour le Projet Transverse

* Jeux de fléchettes et jeux de Handball
* Jeux du type Doodle Jump
* Jeux du type Angry Birds/Flappy Birds, par exemple l'objectif est d'avancer dans le jeu grâce à une catapulte
* Jeux où l'objectif est d'éviter des projectiles volants
* Jeux multijoueur à 2 joueurs où l'objectif est de tirer sur l'autre avec des intéractions avec le décor

## Sujet choisi

> Jeux du type Angry Birds/Doodle Jump, l'objectif est de se catapulter à la verticale vers le haut en visant des plateformes. Lorsque le personnage touche une plateforme, il se place et se fixe sur la plateforme. Le but du jeu est d'atteindre la dernière plateforme et lorsque le personnage tombe, l'utilisateur a perdu

## Contexte et définition du projet

### Base et Contexte du jeu

Le jeu se joue à 1 joueur.Le but du jeu consiste à sauter de plateforme en plateforme verticalement sans tomber
(inspiré de  Doodle Jump) à l'aide d'une catapulte (inspiré d'Angry Bird), le joueur devra viser une plateforme 
à l'aide de sa souris (façon catapulte) afin de monter en altitude, si le joueur tombe de la plateforme la partie se termine.
Le joueur gagne la partie au bout d'une altitude atteinte.

### Fonctionnalités additionnelles sugérées

* Changement de l'environnement au fur et à mesure de l'avancement de la partie 
(obstacle comme monstre ou plante dangereuse,plateforme glissante,vents...)
* Personnalisation du personnage 
* Si le joueur gagne la partie, montre une "vidéo" de félicitation ou autre...
* Le côté gauche de l'écran du jeu est connecté avec le côté droit, permettant ainsi au personnage de passer 
sans difficulté de droite à gauche et vice-versa
* Présence d'objet qui aide le joueur

<!-- Explication du projet -->

## Planning & Délai

<!-- Planning -->

## Organisation

<!-- Cf. organisation.md -->

## Calcul physique

### Contraintes

* Utiliser une ou des trajectoires (parabolique, verticale...)
* Employer des variables (temps, masse...)

### Solutions apportées

* Utilisation d'une catapulte (inspiré d'Angry Birds) pour introduire une ou plusieurs trajectoires paraboliques et verticales
> Mouvement parabolique: Application de la deuxième loi de Newton (F=ma avec F:force, m:masse et a:accélération).

> Le référentiel terrestre peut être considéré comme galiléen ;
On considère le repère Oxy, plan correspondant au mouvement : Ox correspondant à l’horizontale et Oy à la verticale ;
La seule force extérieure au système (le personnage) est le poids ;

> D’après le PFD, on a :
P = ma ⇔ mg = ma ⇔ a = g

> On intègre deux fois le vecteur accélération, que l’on projette sur les deux axes, pour obtenir les équations horaires du système :
a (0, −g) ⇒ v (v0 cos α, − gt + v0 sin α) ⇒ OM (v0 cos α t, - 1/2 gt^2 + v0 sin α t)

> On obtient alors les équations horaires du mouvement suivantes :
x(t) = v0 cos α t
y(t) = − 1/2 gt^2 + v0 sin α t

> Pour obtenir l’équation de la trajectoire, il faut isoler t dans l’équation horaire puis le remplacer dans l’équation horaire :
On a : t = x / v0 cos α

> On remplace : y = − 1/2 g (x / v0 cos α)^2 + v0 sin α (x / v0 cos α)

> On obtient l’équation de la trajectoire suivante : y = (- g / 2v0^2 cos^2 α) x^2 + tan α x

* Emploie de plusieurs variables telles que : l'altitude, la masse, le temps, l'espace, la puissance de la catapulte...

<!-- Calcul physique -->

## Spécification technique

### Contraintes

* Utiliser Python
* Employer des rétroactions (gagné, perdu, conseil...)
* Avoir un rendu graphique

### Solutions apportées

* Utilisation de Python 3.6+ (soit la 3.6, 3.7, 3.8, 3.9 à ce jour)
* Emploie des rétroactions telles que gagné lorsque l'utilisateur atteint une certaine altitude, perdu lorsque l'utilisateur tombe et sort du cadre de l'écran et enfin les conseils par rapport à l'utilisation de la catapulte
* Utilisation de la librairie PyGame pour obtenir un rendu graphique et avoir des interactions avec le jeu
> <!-- Explication de PyGame -->

<!-- Ce qui est lier au code -->
