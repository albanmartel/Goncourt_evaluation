"""
Classe Dao[Course]
"""

from dataclasses import dataclass
from typing import Any

from daos.dao import Dao
from models.author import Author


@dataclass
class AuthorDao(Dao[Author]):
    @staticmethod
    def author_from_db(record: dict) -> Author:
        """
        Construit un auteur à partir des données obtenues par la requête SQL
        Méthode qui permet de passer les données à un objet Auteur
        Args:
            record: le dictionnaire obtenu à partir de la requête SQL

        Returns: Retourne un objet Author
        """
        if record is not None:
            return Author(**record)
        return Author("unknown", "unknown")

    def read(self, id_author: int) -> Author | None:
        """
        Renvoie l'auteur correspondant à l'entité dont l'id est id_auteur
        (ou None s'il n'a pu être trouvé)
        Args:
            id_author: le numéro d'id correspondant à l'auteur recherché

        Returns: Renvoie l'auteur correspondant à l'entité dont l'id est id_auteur
        (ou None s'il n'a pu être trouvé)
        """
        sql = """SELECT auteur.auteur_id AS id_author,
        COALESCE(NULLIF(personne.personne_prenom, 'NULL'), '')  AS first_name,
        personne.personne_nom AS last_name, 
        COALESCE(NULLIF(utilisateur.utilisateur_rue, 'NULL'), '') AS user_street,
        COALESCE(NULLIF(utilisateur.utilisateur_code_postal, 'NULL'), '') AS user_postal_code,
        COALESCE(NULLIF(utilisateur.utilisateur_ville, 'NULL'), '') AS user_city,
        COALESCE(NULLIF(utilisateur.utilisateur_courriel, 'NULL'), '') as user_email,
        COALESCE(NULLIF(utilisateur.utilisateur_telephone, 'NULL'), '') as user_phone,
        COALESCE(NULLIF(auteur.auteur_biographie, 'NULL'), '') AS biography 
        FROM auteur
        LEFT JOIN personne ON personne.personne_id = auteur.personne_id
        LEFT JOIN authentification ON authentification.personne_id = personne.personne_id
        LEFT JOIN utilisateur ON utilisateur.utilisateur_id = authentification.utilisateur_id
        WHERE auteur.auteur_id = (%s);"""

        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(sql, (id_author,))
                record = cursor.fetchone()
                if record is not None:
                    print(record)
                    author = self.author_from_db(record)
                else:
                    author = None

                return author

        except Exception as e:
            print(f"Une exception s'est produite : {e}")

            return None

    def readall(self) -> list[Author]:
        """

        Returns: une liste d'instances d'Author ou
        None si rien n'a été trouvé

        """
        authors: list[Author] = []

        sql = """SELECT auteur.auteur_id AS id_author,
        COALESCE(NULLIF(personne.personne_prenom, 'NULL'), '')  AS first_name,
        personne.personne_nom AS last_name, 
        COALESCE(NULLIF(utilisateur.utilisateur_rue, 'NULL'), '') AS user_street,
        COALESCE(NULLIF(utilisateur.utilisateur_code_postal, 'NULL'), '') AS user_postal_code,
        COALESCE(NULLIF(utilisateur.utilisateur_ville, 'NULL'), '') AS user_city,
        COALESCE(NULLIF(utilisateur.utilisateur_courriel, 'NULL'), '') as user_email,
        COALESCE(NULLIF(utilisateur.utilisateur_telephone, 'NULL'), '') as user_phone,
        COALESCE(NULLIF(auteur.auteur_biographie, 'NULL'), '') AS biography 
        FROM auteur
        LEFT JOIN personne ON personne.personne_id = auteur.personne_id
        LEFT JOIN authentification ON authentification.personne_id = personne.personne_id
        LEFT JOIN utilisateur ON utilisateur.utilisateur_id = authentification.utilisateur_id;"""

        try:
            with Dao.connection.cursor() as cursor:
                cursor.execute(sql)
                records = cursor.fetchall()
                if records is not None:
                    for record in records:
                        authors.append(self.author_from_db(record))
                else:
                    authors = None

                return authors

        except Exception as e:
            print(f"Une exception s'est produite : {e}")

            return None

    def create(self, course: Author) -> int:
        pass

    def update(self, course: Author) -> Any:
        pass

    def delete(self, course: Author) -> Any:
        pass

    def find(self, course: Author) -> Any:
        pass

    def findAll(self, course: Author) -> Any:
        pass

    def findById(self, course: Author, id: int) -> Any:
        pass

    def findAllById(self, course: Author, id: int) -> Any:
        pass

    def findByName(self, course: Author, name: str) -> Any:
        pass

    def findAllByName(self, course: Author, name: str) -> Any:
        pass

    def findAllByIdAndName(self, course: Author, id: int, name: str) -> Any:
        pass

    def findAllByNameAndIdAndName(self, course: Author, id: int, name: str) -> Any:
        pass
