# -*- coding: utf-8 -*-

"""
Classe Book
"""

from dataclasses import dataclass
from datetime import date


@dataclass
class Book():
    """
    Classe Book
    Elle permet de manipuler l'objet livre

    :param book_title: titre du livre concernée
    :param book_summary: Résumé du libre
    :param book_isbn: numéro ISBN uniquement d'un livre est pour référencer une modèle de livre imprimé
    :param book_nbr_pages: nombre de pages
    :param book_price: float
    :param book_minimal_age: âge minimal recommandé pour lire le livre concerné

    """
    book_title: str
    book_summary: str
    book_isbn: str
    book_publication_date: date
    book_nbr_pages: str
    book_price: float
    book_minimal_age: int
