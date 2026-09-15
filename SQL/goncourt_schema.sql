--
-- Base de données : goncourt
--
CREATE DATABASE IF NOT EXISTS goncourt DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_uca1400_ai_ci;
USE goncourt;

-- --------------------------------------------------------

--
-- Structure de la table auteur
--

CREATE TABLE IF NOT EXISTS auteur (
  auteur_id smallint(6) NOT NULL,
  auteur_biographie text DEFAULT NULL,
  personne_id smallint(6) NOT NULL,
  PRIMARY KEY (auteur_id),
  KEY personne_id (personne_id)
) 

-- --------------------------------------------------------

--
-- Structure de la table authentification
--

CREATE TABLE IF NOT EXISTS authentification (
  personne_id smallint(6) NOT NULL,
  utilisateur_id smallint(6) NOT NULL,
  authentification_login varchar(50) DEFAULT NULL,
  authentification_mot_de_passe varchar(50) DEFAULT NULL,
  authentification_role varchar(50) DEFAULT NULL,
  PRIMARY KEY (personne_id,utilisateur_id),
  UNIQUE KEY authentification_login (authentification_login),
  KEY utilisateur_id (utilisateur_id)
) 

-- --------------------------------------------------------

--
-- Structure de la table couvert
--

CREATE TABLE IF NOT EXISTS couvert (
  auteur_id smallint(6) NOT NULL,
  membre_id smallint(6) NOT NULL,
  couvert_num smallint(6) DEFAULT NULL,
  couvert_date_debut date DEFAULT NULL,
  couvert_date_fin varchar(50) DEFAULT NULL,
  couvert_fonction varchar(100) DEFAULT NULL,
  couvert_est_president smallint(6) DEFAULT 0,
  PRIMARY KEY (auteur_id,membre_id),
  UNIQUE KEY couvert_num (couvert_num),
  KEY membre_id (membre_id)
) 

-- --------------------------------------------------------

--
-- Structure de la table editeur
--

CREATE TABLE IF NOT EXISTS editeur (
  editeur_id smallint(6) NOT NULL,
  editeur_nom varchar(50) DEFAULT NULL,
  editeur_francophone smallint(6) DEFAULT NULL,
  PRIMARY KEY (editeur_id)
) 

-- --------------------------------------------------------

--
-- Structure de la table livre
--

CREATE TABLE IF NOT EXISTS livre (
  isbn_livre varchar(13) NOT NULL,
  livre_titre varchar(50) DEFAULT NULL,
  livre_resume text DEFAULT NULL,
  auteur_id smallint(6) NOT NULL,
  PRIMARY KEY (isbn_livre),
  KEY auteur_id (auteur_id)
) 

-- --------------------------------------------------------

--
-- Structure de la table membre
--

CREATE TABLE IF NOT EXISTS membre (
  membre_id smallint(6) NOT NULL,
  membre_historique text DEFAULT NULL,
  PRIMARY KEY (membre_id)
) 

-- --------------------------------------------------------

--
-- Structure de la table parution
--

CREATE TABLE IF NOT EXISTS parution (
  isbn_livre varchar(13) NOT NULL,
  editeur_id smallint(6) NOT NULL,
  parution_isbn int(11) NOT NULL,
  parution_date date DEFAULT NULL,
  parution_nbr_page smallint(6) DEFAULT NULL,
  parution_prix varchar(50) DEFAULT NULL,
  parution_age varchar(50) DEFAULT NULL,
  PRIMARY KEY (isbn_livre,editeur_id),
  UNIQUE KEY parution_isbn (parution_isbn),
  KEY editeur_id (editeur_id)
) 

-- --------------------------------------------------------

--
-- Structure de la table personnage
--

CREATE TABLE IF NOT EXISTS personnage (
  personnage_id smallint(6) NOT NULL,
  personnage_name varchar(50) DEFAULT NULL,
  personnage_description text DEFAULT NULL,
  isbn_livre varchar(13) NOT NULL,
  PRIMARY KEY (personnage_id),
  KEY isbn_livre (isbn_livre)
) 

-- --------------------------------------------------------

--
-- Structure de la table personne
--

CREATE TABLE IF NOT EXISTS personne (
  personne_id smallint(6) NOT NULL,
  personne_first_name varchar(100) NOT NULL,
  personne_last_name varchar(50) DEFAULT NULL,
  PRIMARY KEY (personne_id)
) 

-- --------------------------------------------------------

--
-- Structure de la table prix_litteraire
--

CREATE TABLE IF NOT EXISTS prix_litteraire (
  prix_litteraire_id varchar(50) NOT NULL,
  prix_litteraire_nom varchar(50) DEFAULT NULL,
  prix_litteraire_date date NOT NULL,
  isbn_livre varchar(13) NOT NULL,
  PRIMARY KEY (prix_litteraire_id),
  KEY isbn_livre (isbn_livre)
) 

-- --------------------------------------------------------

--
-- Structure de la table selectionner
--

CREATE TABLE IF NOT EXISTS selectionner (
  isbn_livre varchar(13) NOT NULL,
  membre_id smallint(6) NOT NULL,
  session_id smallint(6) DEFAULT NULL,
  session_date date DEFAULT NULL,
  session_vote smallint(6) DEFAULT NULL,
  session_rang varchar(50) DEFAULT NULL,
  session_nbr_livres smallint(6) DEFAULT NULL,
  session_est_laureat smallint(6) DEFAULT 0,
  PRIMARY KEY (isbn_livre,membre_id),
  UNIQUE KEY session_id (session_id),
  KEY membre_id (membre_id)
) 

-- --------------------------------------------------------

--
-- Structure de la table utilisateur
--

CREATE TABLE IF NOT EXISTS utilisateur (
  utilisateur_id smallint(6) NOT NULL,
  utilisateur_rue varchar(100) DEFAULT NULL,
  utilisateur_ville varchar(100) DEFAULT NULL,
  utilisateur_code_postal char(5) DEFAULT NULL,
  utilisateur_courriel varchar(100) DEFAULT NULL,
  utilisateur_telephone char(10) DEFAULT NULL,
  PRIMARY KEY (utilisateur_id)
) 

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table auteur
--
ALTER TABLE auteur
  ADD CONSTRAINT auteur_ibfk_1 FOREIGN KEY (personne_id) REFERENCES personne (personne_id);

--
-- Contraintes pour la table authentification
--
ALTER TABLE authentification
  ADD CONSTRAINT authentification_ibfk_1 FOREIGN KEY (personne_id) REFERENCES personne (personne_id),
  ADD CONSTRAINT authentification_ibfk_2 FOREIGN KEY (utilisateur_id) REFERENCES utilisateur (utilisateur_id);

--
-- Contraintes pour la table couvert
--
ALTER TABLE couvert
  ADD CONSTRAINT couvert_ibfk_1 FOREIGN KEY (auteur_id) REFERENCES auteur (auteur_id),
  ADD CONSTRAINT couvert_ibfk_2 FOREIGN KEY (membre_id) REFERENCES membre (membre_id);

--
-- Contraintes pour la table livre
--
ALTER TABLE livre
  ADD CONSTRAINT livre_ibfk_1 FOREIGN KEY (auteur_id) REFERENCES auteur (auteur_id);

--
-- Contraintes pour la table parution
--
ALTER TABLE parution
  ADD CONSTRAINT parution_ibfk_1 FOREIGN KEY (isbn_livre) REFERENCES livre (isbn_livre),
  ADD CONSTRAINT parution_ibfk_2 FOREIGN KEY (editeur_id) REFERENCES editeur (editeur_id);

--
-- Contraintes pour la table personnage
--
ALTER TABLE personnage
  ADD CONSTRAINT personnage_ibfk_1 FOREIGN KEY (isbn_livre) REFERENCES livre (isbn_livre);

--
-- Contraintes pour la table prix_litteraire
--
ALTER TABLE prix_litteraire
  ADD CONSTRAINT prix_litteraire_ibfk_1 FOREIGN KEY (isbn_livre) REFERENCES livre (isbn_livre);

--
-- Contraintes pour la table selectionner
--
ALTER TABLE selectionner
  ADD CONSTRAINT selectionner_ibfk_1 FOREIGN KEY (isbn_livre) REFERENCES livre (isbn_livre),
  ADD CONSTRAINT selectionner_ibfk_2 FOREIGN KEY (membre_id) REFERENCES membre (membre_id);
COMMIT;