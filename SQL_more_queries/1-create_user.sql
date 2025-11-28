-- Creates the MySQL user 'user_0d_1' and grants them all global privileges.

-- 1.Create Root user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- 2.Permissions
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- 3.Update
FLUSH PRIVILEGES;
