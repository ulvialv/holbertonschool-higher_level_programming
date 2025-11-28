-- Create user only if it does not already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges on the server
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;
