# -*- coding: utf-8 -*-

"""
Classe Literature_Prize
"""

from dataclasses import dataclass
from datetime import date


@dataclass
class Literature_Prize():
    """
    Classe Literature_Prize

    Cette classe permet gérer les prix littéraires goncourt
    """
    prize_name: str
    prize_date: date

    def toString(self):
        return f"{self.prize_name} {self.prize_date}"