# Projet : Jeu de Blackjack en Python

Ce projet est un **mini-jeu de Blackjack** développé en Python pour tester et améliorer les compétences en algorithmie. Le jeu simule une partie de Blackjack où le joueur affronte l'ordinateur. Le but est de battre le score de l'ordinateur sans dépasser 21.

## Objectifs du Projet

- **Améliorer les compétences en algorithmie** : Ce projet permet de s'entraîner sur la logique en programmant un jeu de cartes interactif.
- **Utilisation de structures de données** : Ce projet fait usage de listes, de conditions, de boucles, et de la gestion d'entrées utilisateur.
- **Respect des règles du Blackjack** : Le jeu suit les règles basiques du Blackjack, incluant la gestion des As, le tirage des cartes, et la comparaison des scores.

## Règles du jeu

1. Le joueur et l'ordinateur reçoivent chacun deux cartes au début de la partie.
2. Le joueur peut voir ses cartes et la première carte de l'ordinateur.
3. Le joueur peut décider de piocher une nouvelle carte ou de passer son tour.
4. L'objectif est d'avoir un score le plus proche possible de 21 sans le dépasser.
5. L'ordinateur continue à piocher des cartes tant que son score est inférieur ou égal à 16.
6. Le joueur gagne si son score est supérieur à celui de l'ordinateur sans dépasser 21 ou si l'ordinateur dépasse 21.

## Fonctionnalités

- **Gestion des As** : Les As valent 11, mais peuvent être convertis en 1 si le total dépasse 21.
- **Comparaison des scores** : À la fin du tour, les scores du joueur et de l'ordinateur sont comparés pour déterminer le gagnant.
- **Rejouer** : Après chaque partie, le joueur peut choisir de rejouer ou de quitter.

## Comment jouer

### 1. Lancer le jeu

En faisant python main.py
Lorsque le script est exécuté, tu seras invité à démarrer une partie de Blackjack :

```bash
Do you want to play a game of Blackjack? Type 'y' or 'n':
