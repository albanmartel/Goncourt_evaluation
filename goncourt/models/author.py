# -*- coding: utf-8 -*-

"""
Classe Author, fille de la classe User
"""

from dataclasses import dataclass
from .user import User

@dataclass
class Author(User):

    """
    L'autheur est un utilisateur qui a une biographie
    et qui écrit un  ou des livres.
    Plutôt tiré par les cheveux comme conception
    """
    biography: str = "unknown"
    book_title: str = "unknown"
    book_summary: str = "unknown"

    def toString(self):
        return f"{self.author_biography}"