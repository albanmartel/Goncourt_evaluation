CREATE TABLE editeur(
   editeur_id SMALLINT (6),
   editeur_nom VARCHAR(50) DEFAULT NULL,
   editeur_francophone SMALLINT (6) DEFAULT 0,
   PRIMARY KEY(editeur_id)
);

CREATE TABLE membre(
   membre_id SMALLINT (6),
   membre_profession VARCHAR(50) DEFAULT NULL,
   membre_historique TEXT DEFAULT NULL,
   PRIMARY KEY(membre_id)
);

CREATE TABLE personne(
   personne_id SMALLINT (6),
   personne_prenom VARCHAR(100) NOT NULL,
   personne_nom VARCHAR(50) DEFAULT NULL,
   PRIMARY KEY(personne_id)
);

CREATE TABLE saison(
   saison_id SMALLINT (6),
   saison_annee SMALLINT NOT NULL (2),
   PRIMARY KEY(saison_id)
);

CREATE TABLE session(
   session_id SMALLINT (6),
   selection_num SMALLINT NOT NULL (6),
   session_date DATE DEFAULT NULL,
   saison_id SMALLINT NOT NULL,
   PRIMARY KEY(session_id),
   FOREIGN KEY(saison_id) REFERENCES saison(saison_id)
);

CREATE TABLE utilisateur(
   utilisateur_id SMALLINT (6),
   utilisateur_rue VARCHAR(100) DEFAULT NULL,
   utilisateur_ville VARCHAR(100) DEFAULT NULL,
   utilisateur_code_postal CHAR(5) DEFAULT NULL,
   utilisateur_courriel VARCHAR(100) DEFAULT NULL,
   utilisateur_telephone CHAR(10) DEFAULT NULL,
   PRIMARY KEY(utilisateur_id)
);

CREATE TABLE auteur(
   auteur_id SMALLINT (6),
   auteur_biographie TEXT DEFAULT NULL,
   personne_id SMALLINT NOT NULL,
   PRIMARY KEY(auteur_id),
   FOREIGN KEY(personne_id) REFERENCES personne(personne_id)
);

CREATE TABLE livre(
   livre_id SMALLINT (6),
   livre_titre VARCHAR(100) DEFAULT NULL,
   livre_resume TEXT DEFAULT NULL,
   auteur_id SMALLINT NOT NULL,
   PRIMARY KEY(livre_id),
   FOREIGN KEY(auteur_id) REFERENCES auteur(auteur_id)
);

CREATE TABLE personnage(
   personnage_id SMALLINT (6),
   personnage_name VARCHAR(50) DEFAULT NULL,
   personnage_description TEXT DEFAULT NULL,
   livre_id SMALLINT NOT NULL,
   PRIMARY KEY(personnage_id),
   FOREIGN KEY(livre_id) REFERENCES livre(livre_id)
);

CREATE TABLE prix_litteraire(
   prix_litteraire_id SMALLINT (6),
   prix_litteraire_nom VARCHAR(50) DEFAULT NULL,
   prix_litteraire_date DATE NOT NULL,
   livre_id SMALLINT NOT NULL,
   PRIMARY KEY(prix_litteraire_id),
   FOREIGN KEY(livre_id) REFERENCES livre(livre_id)
);

CREATE TABLE avoir_couvert(
   auteur_id SMALLINT,
   membre_id SMALLINT,
   couvert_id SMALLINT NOT NULL (6),
   couvert_num SMALLINT NOT NULL (6),
   couvert_date_debut DATE DEFAULT NULL,
   couvert_date_fin DATE DEFAULT NULL,
   couvert_fonction VARCHAR(100) DEFAULT NULL,
   couvert_est_president SMALLINT (6) DEFAULT 0,
   PRIMARY KEY(auteur_id, membre_id),
   FOREIGN KEY(auteur_id) REFERENCES auteur(auteur_id),
   FOREIGN KEY(membre_id) REFERENCES membre(membre_id)
);

CREATE TABLE publier(
   livre_id SMALLINT,
   editeur_id SMALLINT,
   parution_id SMALLINT NOT NULL (6),
   parution_isbn VARCHAR(13) DEFAULT NULL,
   parution_date DATE DEFAULT NULL,
   parution_nbr_page SMALLINT (6) DEFAULT NULL,
   parution_prix DECIMAL(10,2) DEFAULT NULL,
   parution_age VARCHAR(50) DEFAULT NULL,
   PRIMARY KEY(livre_id, editeur_id),
   FOREIGN KEY(livre_id) REFERENCES livre(livre_id),
   FOREIGN KEY(editeur_id) REFERENCES editeur(editeur_id)
);

CREATE TABLE concourir(
   session_id SMALLINT,
   livre_id SMALLINT,
   coucours_id SMALLINT NOT NULL (6),
   concours_votes SMALLINT (6) DEFAULT NULL,
   concours_resultat VARCHAR(50) DEFAULT NULL,
   PRIMARY KEY(session_id, livre_id),
   FOREIGN KEY(session_id) REFERENCES session(session_id),
   FOREIGN KEY(livre_id) REFERENCES livre(livre_id)
);

CREATE TABLE authentifier(
   personne_id SMALLINT,
   utilisateur_id SMALLINT,
   authentification_id SMALLINT NOT NULL (6),
   authentification_login VARCHAR(50) DEFAULT NULL,
   authentification_mot_de_passe VARCHAR(50) DEFAULT NULL,
   authentification_role VARCHAR(50) DEFAULT NULL,
   PRIMARY KEY(personne_id, utilisateur_id),
   FOREIGN KEY(personne_id) REFERENCES personne(personne_id),
   FOREIGN KEY(utilisateur_id) REFERENCES utilisateur(utilisateur_id)
);

CREATE TABLE organiser(
   membre_id SMALLINT,
   saison_id SMALLINT,
   PRIMARY KEY(membre_id, saison_id),
   FOREIGN KEY(membre_id) REFERENCES membre(membre_id),
   FOREIGN KEY(saison_id) REFERENCES saison(saison_id)
);