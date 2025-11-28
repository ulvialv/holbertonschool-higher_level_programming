-- Creates table force_name in the selected database
-- Database name will be given as argument when executing

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL    -- name field cannot be NULL
);
