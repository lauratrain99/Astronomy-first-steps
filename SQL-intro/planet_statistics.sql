/*Find minimum, maximum, average and standard deviation radius
of planets unconfirmed as exoplanets */
SELECT MIN(radius), MAX(radius), AVG(radius), STDDEV(radius) FROM Planet 
WHERE kepler_name IS NULL;