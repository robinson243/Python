# Jeu de Devine le Nombre

## Description

Ce programme est un simple jeu web où les utilisateurs doivent deviner un nombre aléatoire compris entre 0 et 9. À chaque essai, l'application indique si le nombre deviné est trop bas, trop élevé ou correct.

## Prérequis

Avant de pouvoir exécuter ce programme, vous devez avoir installé les éléments suivants :

- [Python 3.6+](https://www.python.org/downloads/)
- Flask : un micro-framework pour Python. Vous pouvez l'installer avec pip.

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/robinson243/Python.git
   cd Python/randomnumber
   ```

2. Installez Flask :

   ```bash
   pip install Flask
   ```

## Utilisation

Pour exécuter le programme, utilisez la commande suivante :

```bash
python project.py
```

### Accéder au Jeu

1. Ouvrez votre navigateur web.
2. Allez à l'URL : [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
3. Vous verrez un message vous invitant à deviner un nombre entre 0 et 9.

### Faire une Devinette

- Ajoutez le nombre que vous devinez à la fin de l'URL. Par exemple :
  - Pour deviner le nombre 4, allez à : [http://127.0.0.1:5000/4](http://127.0.0.1:5000/4)
- L'application vous indiquera si votre essai est trop bas, trop élevé ou correct.

## Fonctionnalités

- Génération d'un nombre aléatoire entre 0 et 9.
- Réponse dynamique basée sur la devinette de l'utilisateur.
- Affichage d'une image GIF pour une meilleure expérience utilisateur.
