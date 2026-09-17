# -*- coding: utf-8 -*-

"""
Classe User, fille de la classe Person
"""
import email
from dataclasses import dataclass
from .person import Person

@dataclass
class User(Person):

    """
    L'author est un auteur qui a une biographie
    Plutôt tiré par les cheveux comme conception
    :param user_email le courriel d'un utilisateur
    :param user_phone le numéro de téléphone

    """
    user_street: str = 0  # nb d'étudiants créés
    user_city: str = "unknown"
    user_postal_code = "unknown"
    user_email: str = "unknown"
    user_phone: str = "unknown"