# -*- coding: utf-8 -*-

"""
Classe abstraite générique Dao[T], dont hérite les classes de DAO de chaque entité
"""
import sys
import os
from pathlib import Path
from dotenv import load_dotenv
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import ClassVar, Optional, Any
import pymysql.cursors
from pymysql import MySQLError

# 1. Charger le .env avant la définition de la classe
load_dotenv()

# Vérification explicite des variables obligatoires
"""Cette exception a été écrite par l'IA gemini"""
if not os.getenv("MYSQL_PASSWORD"):
    raise ValueError(
        "Erreur : La variable MYSQL_PASSWORD est introuvable (fichier .env ou environnement)."
    )

@dataclass
class Dao[T](ABC):
    try :
        database_u: str = os.getenv("MYSQL_DATABASE_GONCOURT")
        """Cette connexion a été écrite par l'IA gemini"""
        connection: ClassVar[pymysql.Connection] = pymysql.connect(
            host=os.getenv("MYSQL_HOST"),
            port=int(os.getenv("MYSQL_PORT", 3306)),
            user=os.getenv("MYSQL_GONCOURT_USER"),
            password=os.getenv("MYSQL_GONCOURT_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE_GONCOURT"),
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=False,  # Message de l'IA : Recommandé si tu gères des transactions (START TRANSACTION / COMMIT
        )
        print(f"Connexion à la base de données: {database_u} réussie !")
    except pymysql.err.Error as e:
        connection = None
        print(f"Erreur de connexion à MariaDB : {e}")
        print(f"Pas de connexion possible avec la base de données {database_u}\nFin du programme")
       # Fin du programme avec code exit 1
        sys.exit(1)

    except MySQLError as e:
        connection = None
        print(f"Erreur MySQL : {e}")
        print(f"Pas de connexion possible avec la base de données {database_u}\nFin du programme")
        # Fin du programme avec code exit 1
        sys.exit(1)


    @abstractmethod
    def create(self, obj: T) -> int:
        """Crée l'entité en BD correspondant à l'objet obj

        :param obj: à créer sous forme d'entité en BD
        :return: l'id de l'entité insérée en BD (0 si la création a échoué)
        """
        ...

    @abstractmethod
    def read(self, id_entity: int) -> Optional[T]:
        """Renvoit l'objet correspondant à l'entité dont l'id est id_entity
           (ou None s'il n'a pu être trouvé)"""
        ...

    @abstractmethod
    def update(self, obj: T) -> bool:
        """Met à jour en BD l'entité correspondant à obj, pour y correspondre

        :param obj: objet déjà mis à jour en mémoire
        :return: True si la mise à jour a pu être réalisée
        """
        ...

    @abstractmethod
    def delete(self, obj: T) -> bool:
        """Supprime en BD l'entité correspondant à obj

        :param obj: objet dont l'entité correspondante est à supprimer
        :return: True si la suppression a pu être réalisée
        """
        ...