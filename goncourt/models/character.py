# -*- coding: utf-8 -*-

"""
Classe Character
"""

from dataclasses import dataclass

@dataclass
class Character():
    """
    Classe Character
    Pour gérer les personnages de livres des écrivains
    """
    character_name: str
    character_description: str

    def toString(self):
        return f"{self.character_name}:\n {self.character_description}"