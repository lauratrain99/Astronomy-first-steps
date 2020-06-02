/*Find name and radius of planets confirmed as exoplanets */
SELECT kepler_name, radius FROM Planet
WHERE kepler_name IS NOT NULL AND radius BETWEEN 1 AND 3;