-- A script that creates a stored procedure that computes
-- the average score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INTEGER)

COMMENT 'Computes the average score for a user'
BEGIN
	DECLARE total_score INTEGER;
	DECLARE project_count INTEGER;

	SELECT SUM(score) INTO total_score
	FROM corrections
	WHERE corrections.user_id = user_id;

	SELECT COUNT(*) INTO project_count
	FROM corrections
	WHERE corrections.user_id = user_id;
	
	-- Update the users table with the computed average score
	UPDATE users
	SET users.average_score = IF(project_count = 0, 0, total_score / project_count)
	WHERE users.id = user_id;
END//
DELIMITER ;
