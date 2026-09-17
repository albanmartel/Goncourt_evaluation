# -*- coding: utf-8 -*-

"""
Classe Goncourt
"""

from dataclasses import dataclass, field
from datetime import date


from daos.author_daos import AuthorDao
from models.author import Author

@dataclass
class Goncourt:
    """Couche métier de l'application de la selection du prix Goncourt,
    reprenant les cas d'utilisation et les spécifications fonctionnelles :
    - courses : liste des cours existants
    - teachers : liste des enseignants
    - students : liste des élèves"""

    Authors: list[Author] = field(default_factory=list, init=False)

    pass

