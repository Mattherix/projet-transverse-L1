Ce document resume la manière dont les membres du projet s'organise.
Tous les membres se doivent de le lire et accepter ce document.

# Rôle
Chaque participant à un rôle precis. Il est à la fois acteur (il fait des tâches) et reviewer (il valide ou non les tâches des autres).
Il n'hésite pas à être critique. 

Le chef de projet est responsable du projet il veille au bon fonctionnement de l'équipe.
Il prend note des réunions (dans un fichier markdown) pour les rapports.

# Réunions
Toutes les semaines le groupe se réunie pour 1 h. Au début de l'heure nous faisons une réunion de maximum 15.

Chaque personne doit répondre individuellement à 3 questions :
* Qu'est-ce qui a été fait depuis la dernière séance ?
* Qu'elles sont les difficultés rencontrées et comment les résoudre ?
* Qu'est-ce qui doit être fait ?

On a une rapide discussion sur ces 3 points, on se les répartie et on forme des groupes de 1 à 3 personnes pour les faire.

# Tâches
Chaque tâche doit être indépendante, précise, estimable (en temps de travail et difficulté), testable et faisable en 1 semaine.

Une tâche se définie sur un ticket (Issue en anglais).

Elle comporte :
* Un titre (ex : "Documentation : Guide d'installation", "Ajout du Système de connexion").
* Une estimation de la difficultés (Facile/Moyen/Difficile) et du temps (ex : "Difficulté : Facile, Temps : 30 min").
* Une section besoin expliquant pourquoi ce que doit résoudre cette tâche (ex : "Il est compliqué d'installer le projet").
* Une section solution expliquant ce qui doit être fait (ex : "Écriture d'un guide d'installation du projet").
* Une section TODO séparés entre le code et les tests.
* Les meta données du ticket :
  * Les personnes assignées sur la tâches (celui/ceux qui travail dessus + les reviewers)
  * Un type sous forme de label
  * La Milestone à laquelle l'issue est associée
  * Les PR associés à l'issue
    
## Type de tâche
Il y a 7 type de tâches :
* Ajout de fonctionnalités "enhancement"
* Un bug "bug"
* Une vulnérabilité "security"
* Une question "question"
* Une recherche sur un sujet "search"
* Une tâche liée à de la documentation "documentation"
* Une tâche liée aux outils utilisés "repo"

## Kanban
Chaque tâche est collée sur un tableau à 4 colonnes.
* Todo : Ce qu'il y a faire
* In Progress : Ce qui est en cours
* In Review : Ce qui est en review
* Done : Ce qui est fait

Les cartes bougent ainsi : Todo -> In Progress <-> In Review -> Done

# MileStone et organisation sur le long terme
Le projet est séparé en plusieurs parties comportant dans tâches, des milestones. Elle on des dates de fin à tenir.

À la fin de chaque milestone on discute de ce qui s'est passé pendant la milestone et de ce qui est améliorable.

Exemple :
* 0 Preparation : Tous ce qui est lié à la préparation du projet et explication des outils et organisation, fini avant le 01/02/2021.
* ...
* n-1 Fin du code : Fin du code, 2 semaines avant le rapport/présentation
* n Rapport : Préparation du rapport/présentation, fin du projet
 