# -*- coding: utf-8 -*-

"""
Classe Session
"""

from dataclasses import dataclass
from datetime import date


@dataclass
class Session():
    """
    Classe Session
    Elle permet de gérer les sessions de sélection du prix Goncourt

    :param session_number est un entier compris entre 1 et 3
    :param season_date est la date de la session considérée
    """
    session_number: int
    season_date: date

    def toString(self):
        return f"Session n°{self.session_number} du:{self.season_date}"