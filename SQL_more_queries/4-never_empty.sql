-- Creates the table id_not_null in the database selected when running mysql
-- If the table already exists, the script should not fail

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,        -- id has default value 1
    name VARCHAR(256)        -- name field (nullable allowed)
);
