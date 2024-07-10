-- A script that creates a table
-- with id(INT, NOT NULL, AUTOINCREMENT, PKEY)
-- email(255, not null, unique)
-- Name (255)
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL, UNIQUE,
	name VARCHAR(255)
	)
