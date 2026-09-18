#  Académie Goncourt

Projet d'évaluation de l'Académy Python/JAVA Facylities Multi Services

## Enoncé

Le prix Goncourt 2026 sera attribué mardi 3 novembre, au restaurant Drouant à Paris, à l'issue de trois sélections successives :

-   mercredi 2/9 : première sélection comportant une liste de 16 romans ;
-   mardi 6/10 : deuxième sélection, réduite à 8 romans ;
-   mardi 27/10 : troisième sélection, révélant les 4 romans finalistes.

Chaque livre porte un titre, est décrit par un résumé, est écrit par un auteur, est publié par un éditeur et comporte un ou plusieurs personnages principaux.
Il est également caractérisé par une date de parution, un nombre de pages, un ISBN et un prix éditeur.
En outre, chaque auteur peut être décrit – de façon optionnelle – par une biographie.

Le jury est constitué des membres de l'académie Goncourt, qui est composée d'un ensemble de personnalités de l'écriture et présidée par l'une d'elles.
Celui-ci établit trois sélections successives et attribue le prix Goncourt à l'auteur du roman primé à l'issue d'un dernier tour de scrutin lors duquel il obtient un certain nombre de voix, suivi par d'autres romans ayant
obtenu moins de voix.

## Objectif

Il est demandé d'écrire une application en mode console permettant :

-   à tout utilisateur d’afficher les livres composant chaque sélection, avec toutes les informations figurant ci-dessus ;
-   au président du jury d’indiquer les livres faisant partie de la deuxième et troisième sélection ;
-  au président du jury d’indiquer le nombre de votes obtenus par chaque livre présent au dernier tour de scrutin ;
-  dans le futur, d’ajouter une authentification pour chaque membre du jury, leur permettant de voter pour les deuxième et troisième sélections, ainsi que pour le lauréat (l’ensemble étant alors calculé automatiquement) ;

L’ensemble des données de départ pourra être entré en dur dans la base de données utilisée, en se limitant à la description détaillée des huit titres des huit premiers auteurs dans l'ordre alphabétique de leur nom, et en ne renseignant pour les autres que le titre, l'auteur et l'éditeur.

## importer le projet 

### Cloner le projet

```
git clone https://github.com/albanmartel/Goncourt_evaluation.git
```

### Création de la base de données

prérequis, il vous faut au minimum un moteur de base données mariadb ou mysql.

Personnellement, j'utilise le client [phpMyAdmin](https://www.phpmyadmin.net/) pour administrer la base de données.

d'autres solutions alternatives d'administration de base de données (application cliente desktop) sans serveurs php/(MySQL ou MariaDB)/(Apache ou Nginx) :
- [DBeaver](https://dbeaver.io/) un client de référence assez universel pour couvrir de nombreuses technologies de bases de données différences  et multi-plateformes moins user frendly que phpMyAdmin.
- [HeidiSQL](https://www.heidisql.com/) un client plus léger et plus user frendly que DBeaver mais pas aussi universel et multi-plateformes

## Assistance IA

1. Utiliser des variables d'environnement pour se connecter à la base mariadb permet de ne pas publier les mots de passes utilisés. Pour pouvoir faire cela, j'ai demandé à l'IA Gemini de me fournir un extrait de code python et de fichier d'environnement ainsi que les bibliothèques nécessaires pour lire le fichier d'environnement 
1. Pour mieux comprendre les code d'erreurs retourné par mariadb à l'exécution de mon code, je lui ai demandé de me fournir une synthèse des codes et de leurs significations. Cette réponse m'a aidé à mieux comprendre qu'il manquait une virgule dans ma requête. 
