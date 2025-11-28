-- Creates the user 'user_0d_1' if it does not already exist, and sets the passwords.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost IDENTIFIET BY 'user_0d_1_pwd';


-- Grants ALL PRIVILEGES globally to the user, with the ability to grant those privileges to others.
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;


-- Reloads the grant tables to ensure the changes take effect immediately.
FLUSH PRIVILEGES;
