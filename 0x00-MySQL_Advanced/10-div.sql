-- creates a function that performs a safe divivison
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER //
CREATE FUNCTION SafeDiv (a INTEGER, b INTEGER)
RETURNS FLOAT
DETERMINISTIC
BEGIN
	DECLARE result FLOAT;
	SET result  = IF(b = 0, 0, a / b);
	RETURN result;
END//
DELIMITER ;
