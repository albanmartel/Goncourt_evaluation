"""
Classe User, fille de la classe Person
"""

from dataclasses import dataclass

from models.person import Person


@dataclass
class User(Person):
    """
    :param user_street: le nom de la rue de l'utilisateur
    :param user_city: le nom de la ville de l'utilisateur
    :param user_postal_code: le code postal de l'adresse de l'utilisateur
    :param user_email le courriel d'un utilisateur
    :param user_phone le numéro de téléphone

    """

    user_street: str = ""
    user_postal_code: str = ""
    user_city: str = ""
    user_email: str = ""
    user_phone: str = ""
