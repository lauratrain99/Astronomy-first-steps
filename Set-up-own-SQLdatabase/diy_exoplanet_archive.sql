/*Create a table inserting csv documents */
CREATE TABLE Star (
  kepler_id INTEGER PRIMARY KEY,
  t_eff INTEGER NOT NULL,
  radius FLOAT NOT NULL
);

COPY Star (kepler_id, t_eff, radius) 
  FROM 'stars.csv' CSV;

CREATE TABLE Planet(
  kepler_id INTEGER REFERENCES Star (kepler_id),
  koi_name VARCHAR(20) PRIMARY KEY,
  kepler_name VARCHAR(20),
  status VARCHAR(20) NOT NULL,
  period FLOAT,
  radius FLOAT,
  t_eq INTEGER
);

COPY Planet (kepler_id, koi_name, kepler_name, status, period, radius, t_eq) 
  FROM 'planets.csv' CSV;
SELECT * FROM Star;
SELECT * FROM Planet;