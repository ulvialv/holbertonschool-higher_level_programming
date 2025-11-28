-- Creates database hbtn_0d_usa if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the created database
USE hbtn_0d_usa;

-- Creates table states if it doesn't already exist
-- id must be unique, auto-generated, not null and primary key
-- name cannot be null
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- unique, auto-generated primary key
    name VARCHAR(256) NOT NULL          -- state name must not be null
);
