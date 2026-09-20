"""
Classe Author, fille de la classe User
"""

from dataclasses import asdict, dataclass

import weakref

from .user import User


@dataclass
class Author(User):
    """
    L'auteur est un utilisateur qui a une biographie
    et qui écrit un ou des livres.
    Plutôt tiré par les cheveux comme conception
    """
    # Registre avec références faibles pour économiser la mémoire
    _instances = weakref.WeakValueDictionary()
    biography: str = "unknown"
    id_author: int = 0

    def __new__(cls, *args, **kwargs):
        """
        Récupération des id_author soit par kwarks ou par args
        Args:
            *args:
            **kwargs:
        """
        id_author = kwargs.get("id_author")

        # 1. Vérifier si l'instance existe déjà
        if id_author is not None and id_author in cls._instances:
            print(f"-> Instance avec ID '{id_author}' existante récupérée.")
            return cls._instances[id_author]

        # 2. Si elle n'existe pas, on la crée
        print(f"-> Création d'une nouvelle instance pour ID '{id_author}'.")
        instance = super().__new__(cls)

        if id_author is not None:
            cls._instances[id_author] = instance

        return instance

    def items(self):
        """
        méthode pour pouvoir itérer comme avec un dictionnaire

        :param self:
        :return: un dictionnaire itérable
        """
        return asdict(self).items()

    def add_biography(self, string_biography: str) -> None:
        """

        Args:
            string_biography: la chaîne de caractère qui remplace
             la précédente chaîne de la biographie de l'auteur

        Returns: None

        """
        self.biography = string_biography

    def __str__(self) -> str:
        """
        Méthode qui permet les données de l'instance de la classe Auteur

        :return: une chaîne de caractère possédant toutes les données de la classe
        """
        return f""{self.id_author} {self.first_name} {self.last_name} {self.biography} {self.user_street} {self.user_postal_code} {self.user_city} {self.user_email} {self.user_phone}"
