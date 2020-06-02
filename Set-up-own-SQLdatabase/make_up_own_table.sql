/*Set up a table with corresponding attributes and constraints */
CREATE TABLE Planet(
  kepler_id INTEGER NOT NULL,
  koi_name VARCHAR(15) NOT NULL UNIQUE ,
  kepler_name VARCHAR(15),
  status VARCHAR(20) NOT NULL,
  radius FLOAT NOT NULL
);

INSERT INTO Planet 
(kepler_id, koi_name, kepler_name, status, radius)
 VALUES(6862328, 'K00865.01', NULL, 'CANDIDATE', 119.021);

INSERT INTO Planet 
(kepler_id, koi_name, kepler_name, status, radius)
 VALUES(10187017, 'K00082.05', 'Kepler-102 b', 'CONFIRMED', 5.286);

INSERT INTO Planet 
(kepler_id, koi_name, kepler_name, status, radius)
 VALUES(10187017, 'K00082.04', 'Kepler-102 c', 'CONFIRMED', 7.071);

SELECT * FROM Planet