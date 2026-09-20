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
    input("Press ENTER to continue...")
    print("Afficher une liste d'auteurs")
    print(goncourt.str_authors())
    print("""Fin de l'application""")
    
if __name__ == '__main__':
    main()
