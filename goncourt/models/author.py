# -*- coding: utf-8 -*-

"""
Classe User, fille de la classe Person
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
    author_biography: str = "unknown"