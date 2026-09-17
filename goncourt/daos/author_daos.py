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
