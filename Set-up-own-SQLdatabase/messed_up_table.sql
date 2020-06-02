/*Fix a corrupted table*/
UPDATE Planet
SET kepler_name = NULL
WHERE status = 'FALSE POSITIVE' OR status = 'CANDIDATE';

DELETE FROM Planet
WHERE radius < 0;
SELECT * FROM Planet;
