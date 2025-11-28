-- Creates the table unique_id in the given database
-- id has default value 1 and must be unique
-- If table exists, script should not fail

CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,     -- unique id with default value 1
    name VARCHAR(256)            -- name column
);
