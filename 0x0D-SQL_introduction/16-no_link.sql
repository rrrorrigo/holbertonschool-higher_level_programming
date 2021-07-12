-- script that lists all records of the table
-- don't list rows without a name value
-- results should display the score and the name
-- Records should be listed by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
