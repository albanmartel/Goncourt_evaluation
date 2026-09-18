# -*- coding: utf-8 -*-

"""
Classe Goncourt
"""

from dataclasses import dataclass, field
from datetime import date
from typing import Optional


from daos.author_daos import AuthorDao
from models.author import Author

@dataclass
class Goncourt:
    """Couche métier de l'application de la selection du prix Goncourt,
    reprenant les cas d'utilisation et les spécifications fonctionnelles :
    - authors : liste des auteurs enregistrés
    - teachers : liste des enseignants
    - students : liste des élèves"""

    Authors: list[Author] = field(default_factory=list, init=False)

    @staticmethod
    def get_author_by_id(id_author: int) -> Optional[Author]:
        author_dao: AuthorDao = AuthorDao()
        return author_dao.read(id_author)

    @staticmethod
    def get_authors() -> Optional[Author]:
        author_dao: AuthorDao = AuthorDao()
        return author_dao.readall()

