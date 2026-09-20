"""
Classe Author, fille de la classe User
"""

from dataclasses import asdict, dataclass

from .user import User


@dataclass
class Author(User):
    """
    L'auteur est un utilisateur qui a une biographie
    et qui écrit un ou des livres.
    Plutôt tiré par les cheveux comme conception
    """

    biography: str = "unknown"
    id_author: int = 0

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
        return f"{self.first_name} {self.last_name} {self.book_title} {self.book_summary} {self.biography} {self.user_street} {self.user_postal_code} {self.user_city} {self.user_email} {self.user_phone}"
