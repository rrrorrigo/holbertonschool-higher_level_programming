-- script that creates an user user_0d_1
-- user_0d_1 should have all privileges on your MySQL server
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
SET PASSWORD FOR 'user_0d_1'@'localhost' = 'user_0d_1_pwdbar';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
