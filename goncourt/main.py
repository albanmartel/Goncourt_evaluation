#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Application de gestion de la selection du prix goncourt
"""

from business.goncourt import Goncourt

def main() ->
    """Programme principal."""
    print("""\
    --------------------------
    Bienvenue dans notre sélection du Goncourt
    --------------------------""")

    goncourt: Goncourt = Goncourt()

    print("""Fin de l'application²²²²²²²²²²²²²²²²²²²²²²""")

if __name__ == '__main__':
    main()