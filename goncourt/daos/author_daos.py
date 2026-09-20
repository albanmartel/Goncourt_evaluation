# -*- coding: utf-8 -*-

"""
Classe Dao[Course]
"""

from models.author import Author
from daos.dao import Dao
from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class AuthorDao(Dao[Author]):

    @staticmethod
    def author_from_db(record) -> Author:
        """Construit un cours du modèle d'après son entité en BD"""
        author: Author = Author(record['first_name'], record['last_name'], record['book_title'], record['book_summary'], record['biography'])
        author.id = record['id_author']

        return author

    def read(self, id_author: int) -> Optional[Author]:
        """
        Renvoit l'autheur correspondant à l'entité dont l'id est id_autheur
        (ou None s'il n'a pu être trouvé)
        """

        sql = """SELECT auteur.auteur_id AS id_author,
        COALESCE(NULLIF(personne.personne_prenom, 'NULL'), '')  AS first_name,
        personne.personne_nom AS last_name, 
        COALESCE(NULLIF(utilisateur.utilisateur_rue, 'NULL'), '') AS user_street,
        COALESCE(NULLIF(utilisateur.utilisateur_code_postal, 'NULL'), '') AS user_postal_code,
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

    def readall(self) -> Optional[Author]:
        """
        Renvoit l'ensemble des auteurs
        (ou None s'il n'a pu être trouvé)
        """
        authors: list[Author] = []

        sql = "SELECT personne.personne_prenom AS first_name, personne.personne_nom AS last_name, "
        sql += "livre.livre_resume AS book_summary, livre.livre_titre AS book_title, "
        sql += "auteur.auteur_biographie AS biography, auteur.auteur_id AS id_author FROM auteur "
        sql += "LEFT JOIN personne ON personne.personne_id = auteur.personne_id "
        sql += "LEFT JOIN livre ON livre.auteur_id = auteur.auteur_id "

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
