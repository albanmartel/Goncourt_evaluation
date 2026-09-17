# -*- coding: utf-8 -*-

"""
Classe Publisher
"""

from dataclasses import dataclass

@dataclass
class Member():

    """
    Classe représentant l'éditeur de livre

    :param publisher_name: Le nom de l'éditeur
    """
    publisher_name: str

    def toString(self):
        return f"{self.publisher_name}"