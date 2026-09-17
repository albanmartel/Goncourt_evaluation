# -*- coding: utf-8 -*-

"""
Classe Examination
"""

from dataclasses import dataclass
from email import message


@dataclass
class Examination():
    """
    Classe Examination
    Elle gère les votes et les résultats des sessions

    :param numb_votes: le nombre de votes exprimé pour un livre souvent cette valeur est vide ou Nulle
    :param examination_status:  permet d'afficher l'état de la candidature après le session
    affiche "ELIMINEE", "RETENUE" ou  "GAGNANTE"
    """
    numb_votes: int
    examination_status: str

    def toString(self):
        message: str = f"Résultat de la sélection: {self.examination_status}"
        if self.numb_votes != None and self.numb_votes.lower != "null":
            message += f" a obtenu: {self.numb_votes}"

        return message