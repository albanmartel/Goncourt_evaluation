# -*- coding: utf-8 -*-

"""
Classe Cutelery cette classe représente les membres de l'académie Goncourt
"""

from dataclasses import dataclass
from datetime import date


@dataclass
class Cutelery():

    """
    Classe Cutelery correspond au jury Goncourt
    qui se tient en général dans un restaurant Drouand
    Chaque académicien Goncourt a un couteau portant un numéro

    :param cutelery_date_start: date d'entrée d'un nouvel auteur en tant qu'académicien
    :param cutelery_date_end: date de sortie d'un académicien Goncourt
    :param cutelery_fonction: fonction occupée par un membre de l'académie quelques uns ont une fonction particulière
    la plupart des autres aucune
    :param is_president: True si l'académicien est président Goncourt
    """
    cutelery_date_start: date
    cutelery_date_end: date
    cutelery_fonction: str
    is_president: bool