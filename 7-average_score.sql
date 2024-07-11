-- A script that creates a stored procedure that computes
-- the average score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INTEGER)

COMMENT 'Computes the average score for a user'
BEGIN
	DECLARE avg_score FLOAT;
	
	IF EXISTS (SELECT 1 FROM users WHERE id = user_id) THEN
		SELECT AVG(score) INTO avg_score
		FROM corrections
		WHERE user_id = user_id;
		
		-- Update the users table with the computed average score
		UPDATE users
		SET average_score = avg_score
		WHERE id = user_id;
	END IF;
END//
DELIMITER ;
