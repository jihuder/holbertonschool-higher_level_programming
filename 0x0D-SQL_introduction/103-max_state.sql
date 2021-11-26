-- Displays the maximum temperature
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY MAX(value) DESC;
