# -*- coding: utf-8 -*-

"""
Classe Authenticate
"""

from dataclasses import dataclass

@dataclass
class Authenticate:
    """
    Classe Authenticate

    Elle est prévue pour être utilisée par la suite
    :param authenticate_login: chaîne de caractère peut être un pseudo ou un email pour permettre l'authentification
    :param authenticate_password: chaîne de caractères pour stocker le mot de passe
    :param authenticate_rights: chaîne de caractères représentant les droits de l'utilisateur
    """
    authenticate_login: str
    authenticate_password: str
    authenticate_rights: str

    def toString(self):
        return f"{self.authenticate_login} {self.authenticate_password} {self.authenticate_rights}"