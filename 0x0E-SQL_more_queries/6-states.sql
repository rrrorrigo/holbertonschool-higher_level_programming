-- script that creates the database hbtn_0d_usa and the table states
-- id INT unique, auto generated, not null. and primary key, name VARCHAR (256)not null
CREATE SCHEMA IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `states` (
       `id` INT UNIQUE NOT NULL AUTO_INCREMENT,
       `name` VARCHAR(256) NOT NULL,
       PRIMARY KEY (id)
);
