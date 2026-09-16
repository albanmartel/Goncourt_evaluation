CREATE DATABASE IF NOT EXISTS goncourt_selection DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_uca1400_ai_ci;
USE goncourt_selection;

CREATE TABLE auteur (
  auteur_id smallint(6) NOT NULL,
  auteur_biographie text DEFAULT NULL,
  personne_id smallint(6) NOT NULL
);

CREATE TABLE authentification (
  personne_id smallint(6) NOT NULL,
  utilisateur_id smallint(6) NOT NULL,
  authentification_login varchar(50) DEFAULT NULL,
  authentification_mot_de_passe varchar(50) DEFAULT NULL,
  authentification_role varchar(50) DEFAULT NULL
); 

CREATE TABLE couvert (
  auteur_id smallint(6) NOT NULL,
  membre_id smallint(6) NOT NULL,
  couvert_num smallint(6) NOT NULL,
  couvert_date_debut date DEFAULT NULL,
  couvert_date_fin date DEFAULT NULL,
  couvert_fonction varchar(100) DEFAULT NULL,
  couvert_est_president smallint(6) DEFAULT 0
);

CREATE TABLE editeur (
  editeur_id smallint(6) NOT NULL,
  editeur_nom varchar(50) DEFAULT NULL,
  editeur_francophone smallint(6) DEFAULT 0
); 

CREATE TABLE livre (
  livre_id smallint(6) NOT NULL,
  livre_titre varchar(50) DEFAULT NULL,
  livre_resume text DEFAULT NULL,
  auteur_id smallint(6) NOT NULL
); 

CREATE TABLE membre (
  membre_id smallint(6) NOT NULL,
  membre_profession varchar(50) DEFAULT NULL,
  membre_historique text DEFAULT NULL
); 

CREATE TABLE parution (
  parution_id smallint(6) NOT NULL,
  livre_id smallint(6) NOT NULL,
  editeur_id smallint(6) NOT NULL,
  parution_isbn varchar(13) DEFAULT NULL,
  parution_date date DEFAULT NULL,
  parution_nbr_page smallint(6) DEFAULT NULL,
  parution_prix decimal(10,2) DEFAULT NULL,
  parution_age varchar(50) DEFAULT NULL
);

CREATE TABLE personnage (
  personnage_id smallint(6) NOT NULL,
  personnage_name varchar(50) DEFAULT NULL,
  personnage_description text DEFAULT NULL,
  livre_id smallint(6) NOT NULL
); 

CREATE TABLE personne (
  personne_id smallint(6) NOT NULL,
  personne_prenom varchar(100) NOT NULL,
  personne_nom varchar(50) DEFAULT NULL
); 

CREATE TABLE prix_litteraire (
  prix_litteraire_id varchar(50) NOT NULL,
  prix_litteraire_nom varchar(50) DEFAULT NULL,
  prix_litteraire_date date NOT NULL,
  livre_id smallint(6) NOT NULL
); 

CREATE TABLE session (
  livre_id smallint(6) NOT NULL,
  membre_id smallint(6) NOT NULL,
  session_id smallint(6) NOT NULL,
  session_date date DEFAULT NULL,
  session_vote smallint(6) DEFAULT NULL,
  session_rang varchar(50) DEFAULT NULL,
  session_nbr_livres smallint(6) NOT NULL,
  session_est_laureat smallint(6) DEFAULT 0
); 

CREATE TABLE utilisateur (
  utilisateur_id smallint(6) NOT NULL,
  utilisateur_rue varchar(100) DEFAULT NULL,
  utilisateur_ville varchar(100) DEFAULT NULL,
  utilisateur_code_postal char(5) DEFAULT NULL,
  utilisateur_courriel varchar(100) DEFAULT NULL,
  utilisateur_telephone char(10) DEFAULT NULL
); 


ALTER TABLE auteur
  ADD PRIMARY KEY (auteur_id),
  ADD KEY personne_id (personne_id);

ALTER TABLE authentification
  ADD PRIMARY KEY (personne_id,utilisateur_id),
  ADD UNIQUE KEY authentification_login (authentification_login),
  ADD KEY utilisateur_id (utilisateur_id);

ALTER TABLE couvert
  ADD PRIMARY KEY (auteur_id),
  ADD KEY membre_id (membre_id),
  ADD KEY auteur_id (auteur_id,membre_id);

ALTER TABLE editeur
  ADD PRIMARY KEY (editeur_id);

ALTER TABLE livre
  ADD PRIMARY KEY (livre_id),
  ADD KEY auteur_id (auteur_id);

ALTER TABLE membre
  ADD PRIMARY KEY (membre_id);

ALTER TABLE parution
  ADD PRIMARY KEY (livre_id,editeur_id),
  ADD UNIQUE KEY parution_id (parution_id),
  ADD KEY livre_id (livre_id),
  ADD KEY parution_ibfk_2 (editeur_id);

ALTER TABLE personnage
  ADD PRIMARY KEY (personnage_id),
  ADD KEY livre_id (livre_id);

ALTER TABLE personne
  ADD PRIMARY KEY (personne_id);

ALTER TABLE prix_litteraire
  ADD PRIMARY KEY (prix_litteraire_id),
  ADD KEY livre_id (livre_id);

ALTER TABLE session
  ADD PRIMARY KEY (livre_id,membre_id),
  ADD UNIQUE KEY session_id (session_id),
  ADD KEY membre_id (membre_id);

ALTER TABLE utilisateur
  ADD PRIMARY KEY (utilisateur_id);


ALTER TABLE auteur
  ADD CONSTRAINT auteur_ibfk_1 FOREIGN KEY (personne_id) REFERENCES personne (personne_id);

ALTER TABLE authentification
  ADD CONSTRAINT authentification_ibfk_1 FOREIGN KEY (personne_id) REFERENCES personne (personne_id),
  ADD CONSTRAINT authentification_ibfk_2 FOREIGN KEY (utilisateur_id) REFERENCES utilisateur (utilisateur_id);

ALTER TABLE couvert
  ADD CONSTRAINT couvert_ibfk_1 FOREIGN KEY (auteur_id) REFERENCES auteur (auteur_id),
  ADD CONSTRAINT couvert_ibfk_2 FOREIGN KEY (membre_id) REFERENCES membre (membre_id);

ALTER TABLE livre
  ADD CONSTRAINT livre_ibfk_1 FOREIGN KEY (auteur_id) REFERENCES auteur (auteur_id);

ALTER TABLE parution
  ADD CONSTRAINT parution_ibfk_1 FOREIGN KEY (livre_id) REFERENCES livre (livre_id),
  ADD CONSTRAINT parution_ibfk_2 FOREIGN KEY (editeur_id) REFERENCES editeur (editeur_id);

ALTER TABLE personnage
  ADD CONSTRAINT personnage_ibfk_1 FOREIGN KEY (livre_id) REFERENCES livre (livre_id);

ALTER TABLE prix_litteraire
  ADD CONSTRAINT prix_litteraire_ibfk_1 FOREIGN KEY (livre_id) REFERENCES livre (livre_id);

ALTER TABLE session
  ADD CONSTRAINT session_ibfk_1 FOREIGN KEY (livre_id) REFERENCES livre (livre_id),
  ADD CONSTRAINT session_ibfk_2 FOREIGN KEY (membre_id) REFERENCES membre (membre_id);
