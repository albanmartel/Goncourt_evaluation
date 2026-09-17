-- 1. Créer l'utilisateur president
CREATE USER 'president'@'%' IDENTIFIED BY 'GOzR(6Pk@03i!gTQ';

-- 2. Donner tous les droits au président sur la base goncourt_selection
GRANT ALL PRIVILEGES ON goncourt_selection.* TO 'president'@'%';

-- 3. Valider les changements et le recharger
FLUSH PRIVILEGES;