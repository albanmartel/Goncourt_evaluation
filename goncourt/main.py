#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion de la selection du prix goncourt
"""

from business.goncourt import Goncourt

def main() -> None:
    """Programme principal."""
    print("""\
    --------------------------
    Bienvenue dans notre sélection du Goncourt
    --------------------------""")

    goncourt: Goncourt = Goncourt()
    print("Afficher le premier auteur")
    print(goncourt.get_author_by_id(1))
    for key, value in author.__dict__.items():
        print(f"{key} :\n {value}")
    input("Press ENTER to continue...")
    print("Afficher une liste d'auteur par prénom, nom et titre de roman")
    authors: list[Author] = goncourt.get_authors()
    for author in authors:
        print(f"{author.first_name} {author.last_name} {author.book_title}")

    print("""Fin de l'application""")

if __name__ == '__main__':
    main()
