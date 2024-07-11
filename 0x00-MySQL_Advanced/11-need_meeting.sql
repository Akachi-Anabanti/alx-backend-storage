-- creates a view that returns a list of students with
-- scores less hthan 80 and no lastmeeting or more than 1 month
CREATE OR REPLACE VIEW need_meeting AS
	SELECT name FROM students
	WHERE students.score < 80 AND 
		(
			students.last_meeting IS NULL
			OR students.last_meeting < SUBDATE(CURRENT_DATE(), INTERVAL 1 MONTH)
		)
;
