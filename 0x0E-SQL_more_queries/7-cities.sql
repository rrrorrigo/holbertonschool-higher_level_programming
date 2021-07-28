-- script that creates the database hbtn_0d_usa and the table cities
-- VALUES: id PRIMARY KEY, state_id FOREIGN KEY from id of states, name
CREATE SCHEMA IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
       id INT UNIQUE AUTO_INCREMENT NOT NULL,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,
       PRIMARY KEY (id),
       FOREIGN KEY (state_id) REFERENCES states(id)
);
