-- creates an index idx_name_first on the table name and the first letter of the name
CREATE INDEX idx_name_first_score ON names(name(1), score);
