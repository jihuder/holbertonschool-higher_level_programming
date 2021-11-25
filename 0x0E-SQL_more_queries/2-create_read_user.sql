-- Creates a user and database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT ALL ON *.* TO user_0d_2@localhost;
GRANT SELECT ON *.* TO user_0d_2@localhost;
