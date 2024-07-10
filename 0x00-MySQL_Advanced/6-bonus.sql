-- Procedure to add Bonus to a project score
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER //
CREATE PROCEDURE AddBonus(IN user_id INTEGER,
	IN project_name VARCHAR(255),
	IN score INTEGER)
COMMENT 'Adds a correction to the student score for the given project'
BEGIN
	DECLARE proj_id INTEGER;

	-- Check if project exist; if not, insert it
	IF (SELECT id FROM projects WHERE name = project_name) IS NULL THEN
		INSERT INTO projects (name) VALUES(project_name);
	END IF;

	SELECT id INTO proj_id FROM projects
	WHERE name = project_name;
	INSERT INTO corrections(user_id, project_id, score)
	VALUES (user_id, proj_id, score);
END //
DELIMITER ;
