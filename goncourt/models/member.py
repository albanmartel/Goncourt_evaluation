# -*- coding: utf-8 -*-

"""
Classe Members, fille de la classe Author
"""

from dataclasses import dataclass
from .author import Author

@dataclass
class Member(Author):

    """
    Un membre de l'académie Goncours
    est aussi un écrivain auquel l'on ajoute une activité professionnelle
    et un contexte de prise de couvert
    """
    professionnal_activity: str = "unknown"
    member_history_context: str = "unknown"