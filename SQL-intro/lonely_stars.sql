/*Find kepler_id, temperature and radius for all stars
which haven't got a planet as join partner*/
SELECT S.kepler_id, S.t_eff, S.radius
FROM Star S
LEFT OUTER JOIN Planet P USING (kepler_id)
WHERE P.koi_name IS NULL
ORDER BY S.t_eff DESC;