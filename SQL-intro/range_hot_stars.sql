/*Find ID and temperautre of the stars whose temperatures
lie between 5000 and 6000 K*/
SELECT kepler_id, t_eff FROM  Star
WHERE t_eff BETWEEN 5000 AND 6000;