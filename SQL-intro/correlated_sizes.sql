/*Find the radii of those planets 
which orbit the five largest stars*/
SELECT P.koi_name, P.radius, S.radius
FROM Star S
JOIN Planet P USING (kepler_id)
WHERE S.radius IN (
  SELECT S.radius FROM Star S
  ORDER BY S.radius DESC
  LIMIT 5
);
