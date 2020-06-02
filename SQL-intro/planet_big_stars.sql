/*Count the number of planets in each solar system 
where the corresponding stars are larger than our sun*/
SELECT Star.radius, COUNT(Star.kepler_id)
FROM Star 
JOIN Planet ON Star.kepler_id = Planet.kepler_id AND Star.radius > 1
GROUP BY Star.kepler_id
HAVING COUNT(Star.kepler_id) > 1
ORDER BY Star.radius DESC;
