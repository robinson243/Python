# Blog Minimaliste - Day 57

Ce projet est une application web de blog minimaliste développée en **Flask**. Il permet d'afficher des articles récupérés via une API externe. L'utilisateur peut consulter la liste des articles ainsi que leur contenu détaillé.

## Fonctionnalités

- **Affichage de la liste des articles** : Les articles sont récupérés depuis une API externe et affichés sur la page d'accueil.
- **Affichage des détails d'un article** : Chaque article possède une page dédiée affichant son contenu complet.
- **Gestion dynamique des articles** : Les articles sont gérés dynamiquement grâce à l'API JSON et aux templates Flask.

## Technologies utilisées

- **Python 3**
- **Flask** : Framework web utilisé pour gérer les routes et les templates.
- **HTML & Jinja2** : Utilisés pour le rendu dynamique des pages web.
- **CSS** : Pour le style des pages.
- **Requests** : Utilisé pour interagir avec l'API externe et récupérer les données JSON.

## Installation

1. **Cloner le dépôt** :

    ```bash
    git clone https://github.com/robinson243/Python.git
    ```

2. **Accéder au répertoire du projet** :

    ```bash
    cd Python/day57/blog
    ```

3. **Créer un environnement virtuel** (optionnel mais recommandé) :

    ```bash
    python -m venv env
    source env/bin/activate  # Sur Windows : env\Scripts\activate
    ```

4. **Installer les dépendances** :

    ```bash
    pip install flask requests
    ```

5. **Lancer l'application Flask** :

    ```bash
    flask run
    ```

6. **Accéder à l'application** :

    Ouvrez votre navigateur et allez à l'adresse suivante :  
    `http://127.0.0.1:5000`

## Structure des fichiers

- `app.py` : Contient le code principal de l'application Flask, gérant les routes et l'affichage des articles.
- `templates/` : Dossier contenant les templates HTML (utilisant Jinja2 pour le rendu dynamique des pages).
    - `index.html` : Page d'accueil affichant la liste des articles.
    - `post.html` : Page de détail pour afficher un article spécifique.
- `static/` : Contient les fichiers statiques comme les styles CSS.
    - `styles.css` : Fichier CSS pour le style de l'application.

## Explication du code

- **`app.py`** :
    - Récupère les données des articles à partir de l'API externe via `requests.get()`.
    - La route `/` affiche la page d'accueil avec la liste des articles.
    - La route `/post/<index>` permet d'afficher un article spécifique en fonction de son ID.

- **Templates HTML** :
    - **`index.html`** : Affiche la liste des articles avec un lien "Read" pour consulter chaque article.
    - **`post.html`** : Affiche le contenu complet de l'article sélectionné.

## API utilisée

L'application récupère les données des articles via une API JSON externe hébergée sur **npoint.io**. L'URL de l'API est la suivante :

```plaintext
https://api.npoint.io/c790b4d5cab58020d391
