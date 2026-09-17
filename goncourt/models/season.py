# -*- coding: utf-8 -*-

"""
Classe Season
"""

from dataclasses import dataclass


@dataclass
class Season():
    """
    Classe Season

    Elle permet de gérer les saisons littéraires par année
    :param season_year: paramètre de l'année de la saison considérée
    """
    season_year: str

    def toString(self):
        return f"{self.season_year}"