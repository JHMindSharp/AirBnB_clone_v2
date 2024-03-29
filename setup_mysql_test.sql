-- Création de la base de données pour les tests
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
USE hbnb_test_db;

-- Création d'un nouvel utilisateur pour les tests
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Attribution des privilèges sur la base de données de test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Attribution du privilège SELECT sur performance_schema (si nécessaire)
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Application des privilèges
FLUSH PRIVILEGES;
