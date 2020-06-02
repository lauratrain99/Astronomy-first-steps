/*Find number of planets in multi-planet system */
SELECT  kepler_id, COUNT(kepler_id) FROM Planet
GROUP BY kepler_id
HAVING COUNT(koi_name) > 1
ORDER BY COUNT(koi_name) DESC;
