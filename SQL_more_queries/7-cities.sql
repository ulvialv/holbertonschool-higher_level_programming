-- Creates database hbtn_0d_usa if it already doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Selects the database to work in
USE hbtn_0d_usa;

-- Creates table cities with foreign key constraint
-- id: unique, auto generated, not null, primary key
-- state_id: must exist in states table, not null, FK
-- name: cannot be null
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,         -- unique auto-generated id
    state_id INT NOT NULL,                     -- must reference states table
    name VARCHAR(256) NOT NULL,                -- city name cannot be null
    FOREIGN KEY (state_id) REFERENCES states(id)   -- foreign key constraint
);
