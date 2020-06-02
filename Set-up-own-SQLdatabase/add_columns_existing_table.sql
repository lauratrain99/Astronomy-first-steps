/*Add two columns (right ascension and declination) to the existing Star table */
DELETE FROM Star;

ALTER TABLE Star
ADD COLUMN ra FLOAT,
ADD COLUMN decl FLOAT;

COPY Star (kepler_id, t_eff, radius, ra, decl)
  FROM 'stars_full.csv' CSV;
  
SELECT * FROM Star;