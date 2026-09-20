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

#### 1. Créer la base et les tables

A l'aide du script SQL : [goncourt_schema.sql](SQL/goncourt_schema.sql).

#### 2. "Hydrater / peupler" la base de données

A l'aide du script SQL **en déactivant la vérification des clefs étrangères** : [goncourt_data.sql](SQL/data.sql).

#### 3. Créer un utilisateur privilégier de la base de données

A l'aide du script SQL (personnaliser le nom et le mot de passe à votre convenance ): [creer_utilisateur_privilegier_sur_BDD_goncourt_selection.sql](SQL/creer_utilisateur_privilegier_sur_BDD_goncourt_selection.sql)

### Créer un fichier d'environnement

Ce type de fichier permet de protéger l'accès et ne pas divulger ses informations dans un dépôt git

Exemple de contenu pour le fichier __.env__ :
```
MYSQL_ROOT_PASSWORD='<mot_de_passe_root>'
MYSQL_HOST='127.0.0.1'
MYSQL_PORT='3306'
MYSQL_GONCOURT_PASSWORD='<mot_de_passe_utilisateur>'
MYSQL_GONCOURT_USER='<nom_utilisateur>'
MYSQL_DATABASE_GONCOURT='<nom de la base de données>'
```

Note : *Toutes les valeurs comprises entre < et > doivent être personnalisées*

###  Créer un environnement virtuel Python

#### 1. Création et emplacement de l'environnement

À la racine de ton projet :

```bash
python -m venv .venv
```

#### 2. Activation de l'environnement virtuel

Ouvre ton terminal dans le dossier racine de ton projet :

* **Windows (Command Prompt / `cmd.exe`)** :
```cmd
.venv\Scripts\activate.bat
```


* **Windows (PowerShell)** :
```powershell
.venv\Scripts\Activate.ps1
```

*(Si une erreur d'exécution de script apparaît, lance d'abord `Set-ExecutionPolicy Unrestricted -Scope Process` dans ta session).*
* **Linux / macOS** :
```bash
source .venv/bin/activate
```

*`(.venv)` s'affiche au début de la ligne de commande quand l'environnement virtuel est activé.*

Le fichier **.env** doit être enregister à la base du projet

#### 3. Installation des dépendances depuis `requirements.txt`

Contenu de requirements.txt à la base du projet :
```txt
# --- Chiffrement & Sécurité ---
# Dépendances bas niveau pour cryptography
cffi~=2.0
pycparser~=2.23
# SSL et chiffrement
cryptography~=46.0

# --- Gestionnaire de paquets & Formatage ---
uv~=0.9
ruff~=0.9

# --- Base de données ---
PyMySQL~=1.1
types-PyMySQL~=1.1

# --- Configuration & Environnement ---
python-dotenv~=1.0

# --- Documentation ---
pydocstyle~=6.3
sphinx~=7.2
mkdocs~=1.5
mkdocstrings[python]~=0.24
doq~=0.9

# --- Qualité de code & Sécurité ---
mypy~=1.8.0
flake8~=7.0
bandit~=1.7
radon~=6.0

# --- Intégration continue ---
pre-commit~=4.1.0
``` 

Une fois le fichier enregistré, exécuter dans le terminal :

```bash
pip install -r requirements.txt
```

### Alternative plus moderne au fichier requirements : `pyproject.toml`

Crée le fichier `pyproject.toml` à la racine de ton projet.
```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "goncourt-evaluation"
version = "0.1.0"
requires-python = ">=3.14"
dependencies = [
    "bandit>=1.9.4",
    "cffi>=2.1.1",
    "cryptography>=3.0.0",
    "flake8>=7.3.0",
    "doq>=0.9.1",
    "mkdocs>=1.6.1",
    "mkdocstrings>=1.0.6",
    "mypy>=2.3.1",
    "pre-commit>=4.6.2",
    "pydocstyle>=6.3.0",
    "pymysql>=1.2.3",
    "python-dotenv>=1.2.3",
    "radon>=6.0.1",
    "ruff>=0.9.0",
    "sphinx>=9.1.0",
    "types-pymysql>=1.2.0.20260807",
]

[tool.setuptools.packages.find]
where = ["."]
include = ["goncourt*"]

[tool.uv]
link-mode = "copy"

[project.scripts]
goncourt = "goncourt.main:cli"

[tool.ruff]
# Longueur maximale des lignes
line-length = 88

# Version minimale de Python ciblée
target-version = "py311"

# Dossiers à ignorer
exclude = [
    ".git",
    ".venv",
    "__pycache__",
    "build",
    "dist",
]

[tool.ruff.lint]
# Règles à activer
select = [
    "E",   # Error (pycodestyle)
    "W",   # Warning (pycodestyle)
    "F",   # Pyflakes (erreurs de variables non utilisées, imports, etc.)
    "I",   # isort (tri automatique des imports)
    "B",   # flake8-bugbear (détection de bugs fréquents)
    "UP",  # pyupgrade (modernisation de la syntaxe Python)
]

# Règles spécifiques à ignorer si besoin
ignore = [
    "E501", # Laisse le formateur gérer la longueur des lignes au lieu de lever une erreur
]

# Autoriser la correction automatique pour toutes les règles activées
fixable = ["ALL"]

[tool.ruff.lint.isort]
# Combine les imports du même package sur une seule ligne
combine-as-imports = true
```
#### Installer l'outil UV

uv est un outil écrit en Rust (un langage bas niveau équivalent à du C mais avec plus sécurité).
C'est pour cette raison que l'installation des packages est de 10 à 100 fois plus rapide

```bash
pip install uv
```

#### Installer les paquets avec UV

```
uv sync
```


### Intégration continue `pre-commit`

Pour régler la sévérité de **Bandit** et **Radon** afin d'éviter les faux positifs, la configuration se fait directement au niveau des arguments passés dans le fichier `.pre-commit-config.yaml`.

Crée le fichier `.pre-commit-config.yaml` à la racine de ton projet.

#### 1. `.pre-commit-config.yaml`

```yaml
repos:
  - repo: local
    hooks:
      - id: flake8
        name: flake8
        entry: uv run flake8
        language: system
        types: [python]
        args: ["--max-line-length=88", "--ignore=E203,W503", "goncourt/"]
        pass_filenames: false

      - id: mypy
        name: mypy
        entry: uv run mypy
        language: system
        types: [python]
        args: ["--ignore-missing-imports", "goncourt/"]
        pass_filenames: false

      - id: pydocstyle
        name: pydocstyle
        entry: uv run pydocstyle
        language: system
        types: [python]
        args: ["--match-dir=^(?!tests|docs|\\.venv).*", "goncourt/"]
        pass_filenames: false

      - id: bandit
        name: bandit (sécurité - sévérité moyenne+)
        entry: uv run bandit
        language: system
        types: [python]
        # -ll : Medium/High severity, -ii : Medium/High confidence
        args: ["-r", "goncourt/", "-ll", "-ii", "-x", "tests/"]
        pass_filenames: false

      - id: radon
        name: radon (complexité cyclomatique >= C)
        entry: uv run radon cc
        language: system
        types: [python]
        # -n C : alerte uniquement à partir de la note C (complexité modérée/élevée)
        args: ["goncourt/", "-n", "C", "-a"]
        pass_filenames: false
```
### Activer pre-commit

Une fois les paquets installés (`pip install -r requirements.txt`), lancez :

```bash
pre-commit install
```

## Architecture finale d'installation du projet

A ce stade votre architecture ressemble à cela :

```text
Goncourt_evaluation/
│
├── .git/                     # Dossier Git (versionnement)
├── .gitignore                # configurer ce qui est ignoré par Git
├── .venv/                    # Environnement virtuel local
├── .env                      # Variables d'environnement locales
├── .env.example              # Modèle de .env (sans vraies clés)
│
├── .pre-commit-config.yaml   # Orchestration des crochets Pre-Commit
├── requirements.txt          # Export des dépendances
├── pyproject.toml            # Configuration pyproject "Le fichier de manifeste"
├── README.md                 # Documentation de premier niveau
│
├── goncourt/                 # Code source du projet
|    └── business/
|    ├───daos
|    └───models
├───IA_Gemini
├───SQL
└───UML
    ├───1-user_case
    ├───2-class
    ├───3-sequence
    └───4-mcd
```

## Exécuter le code

A ce stade vous devriez pouvoir exécuter le code ou utiliser ce projet pour en poursuivre l'intégration.


### Sur Windows (CMD) :

```cmd
.venv\Scripts\activate.bat
set PYTHONPATH=goncourt && python -m goncourt.main

```

### Sur Windows (PowerShell) :

```powershell
.venv\Scripts\Activate.ps1
$env:PYTHONPATH="goncourt"; python -m goncourt.main

```

### Sur Mac / Linux :

```bash
source .venv/bin/activate
PYTHONPATH=goncourt python3 -m goncourt.main
```

## Assistance IA

1. Utiliser des variables d'environnement pour se connecter à la base mariadb permet de ne pas publier les mots de passes utilisés. Pour pouvoir faire cela, j'ai demandé à l'IA Gemini de me fournir un extrait de code python et de fichier d'environnement ainsi que les bibliothèques nécessaires pour lire le fichier d'environnement 
1. Pour mieux comprendre les code d'erreurs retourné par mariadb à l'exécution de mon code, je lui ai demandé de me fournir une synthèse des codes et de leurs significations. Cette réponse m'a aidé à mieux comprendre qu'il manquait une virgule dans ma requête.
1. Utiliser un environnement d'intégration continue pour faire régulièrement (au moment du commit de git) et lancer un analyse de code (flake8, mypy, pydocstyle, bandit, radon)
1. Se documenter sur  l'utilisation de `pyproject.toml` pour la configuration centralisée d'un projet python.
