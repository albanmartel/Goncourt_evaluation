# -*- coding: utf-8 -*-

"""
Classe Cutelery cette classe représente les membres de l'académie Goncourt
"""

from dataclasses import dataclass
from datetime import date
from xml.etree.ElementTree import tostring


@dataclass
class Cutelery():

    """
    Classe Cutelery correspond au jury Goncourt
    qui se tient en général dans un restaurant Drouand
    Chaque académicien Goncourt a un couteau portant un numéro

    :param cutelery_date_start: date d'entrée d'un nouvel auteur en tant qu'académicien
    :param cutelery_date_end: date de sortie d'un académicien Goncourt
    :param cutelery_fonction: fonction occupée par un membre de l'académie quelques-uns ont une fonction particulière
    la plupart des autres aucune
    :param is_president: True si l'académicien est président Goncourt
    """
    cutelery_date_start: date
    cutelery_date_end: date
    cutelery_fonction: str
    is_president: bool

    def toString(self):
        """
        La méthode affiche tous les paramètres sous forme de string
        la construction de la chaîne change en fonction des paramètres:
        de date de fin
        du booléen est président
        et si une fonction particulière est assignée au membre goncourt

        :return: la chaîne de caractère construite
        """
        message: str = f"L'académicien Goncourt "
        if self.is_president:
            message += f" est président. La personne est entrée le {self.cutelery_date_start.strftime('%d/%m/%Y')}"
        else:
            message += f" n'est pas président."
            if self.cutelery_fonction is not None and self.cutelery_fonction != "" and self.cutelery_fonction.lower() != "null":
                message += f" La personne remplit la fonction de: {self.cutelery_fonction}"
            else:
                message += f" La personne ne rempli aucune fonction particulière."

        message += f" Elle est entrée le {self.cutelery_date_start.strftime('%d/%m/%Y')}"
        if self.cutelery_date_end is None or self.cutelery_date_end == "" or self.cutelery_fonction.lower() != "null":
            message += "Elle est toujours en activité au niveau de l'académie."

        return message