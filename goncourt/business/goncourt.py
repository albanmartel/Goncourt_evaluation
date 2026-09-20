"""
Classe Goncourt
"""

from dataclasses import dataclass, field

from daos.author_daos import AuthorDao
from models.author import Author


@dataclass
class Goncourt:
    """
    Couche métier de l'application de la selection du prix Goncourt,
    reprenant les cas d'utilisation et les spécifications fonctionnelles :
    - authors : liste des auteurs enregistrés
    - members : liste des membres du jury

    """

    Authors: list[Author] = field(default_factory=list, init=False)

    @staticmethod
    def get_author_by_id(id_author: int) -> Author | None:
        """
        Méthode pour obtenir un auteur depuis la classe business
        Goncourt

        Args:
            id_author: l'id de l'auteur recherché

        Returns: un objet DaoAuthor

        """
        author_dao: AuthorDao = AuthorDao()
        return author_dao.read(id_author)

    @staticmethod
    def get_authors() -> Author | None:
        """
        Méthode pour obtenir l'ensemble des auteurs depuis
        la classe business Goncourt
        Returns:

        """
        author_dao: AuthorDao = AuthorDao()
        return author_dao.readall()

    @staticmethod
    def str_author_by_id(id_author: int) -> str:
        """
        Méthode pour obtenir un auteur depuis la classe business
        Goncourt

        Args:
            id_author: l'id de l'auteur recherché

        Returns: une chaîne de caractère de l'objet DaoAuthor

        """
        message_string: str = "Pas de donnée retournée"
        author_dao: AuthorDao = AuthorDao()
        author: Author = author_dao.read(id_author)

        if author is not None:
            message_string = author.__str__()

        return message_string

    @staticmethod
    def str_authors() -> str:
        """
        Méthode pour obtenir une liste d'auteurs depuis la classe business
        Goncourt

        Returns: une chaîne de caractère de la liste d'auteurs
        """
        message_string: str = "Pas de donnée retournée"
        author_dao: AuthorDao = AuthorDao()
        authors: list[Author] = author_dao.readall()

        if authors is not None:
            message_string = ""
            for index, author in enumerate(authors, start=1):
                message_string += f"--- Auteur N°{index} ---\n"
                message_string += f"{author.__str__()}\n"

        return message_string
