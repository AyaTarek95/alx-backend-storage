-- Create index idx_name_first on the table names and the first letter of name
-- DROP INDEX idx_name_first;
CREATE INDEX idx_name_first ON names (name(1)); 
