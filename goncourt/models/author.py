# -*- coding: utf-8 -*-

"""
Classe Author, fille de la classe User
"""

from dataclasses import dataclass
from .user import User

@dataclass
class Author(User):

    """
    L'auteur est un utilisateur qui a une biographie
    et qui écrit un  ou des livres.
    Plutôt tiré par les cheveux comme conception
    """
    biography: str
    id_author: int

    def items(self):
        """
        méthode pour pouvoir itérer comme avec un dictionnaire
        """
        yield "first_name", self.first_name
        yield "last_name", self.last_name
        yield "book_title", self.book_title
        yield "book_summary", self.book_summary
        yield "biography", self.biography
        yield 'id_author', self.id_author
        yield 'user_street', self.user_street
        yield 'user_postal_code', self.user_postal_code
        yield 'user_city', self.user_city
        yield 'user_email', self.user_email
        yield 'user_phone', self.user_phone

    def toString(self):
        return f"{self.author_biography}"
