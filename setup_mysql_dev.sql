-- Création de la base de données s'elle n'existe pas déjà
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Création de l'utilisateur s'il n'existe pas déjà
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Attribution des privilèges sur la base de données de développement
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Attribution du privilège SELECT sur la base de données performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- Application des privilèges
FLUSH PRIVILEGES;
