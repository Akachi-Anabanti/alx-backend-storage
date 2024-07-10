-- A scrip that creates a trigger that decreases the quantity of an item after adding a new order
DROP TRIGGER IF EXISTS decr_qnty;
DELIMITER $$
CREATE TRIGGER decr_qnty
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
		SET quantity = quantity - NEW.number
		WHERE name = NEW.item_name;
END $$
DELIMITER ;
