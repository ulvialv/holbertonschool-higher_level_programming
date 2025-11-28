-- Lists all cities of California in ascending order by city id
-- Uses a subquery to get the id of California from states table
-- Database name will be passed as argument to mysql command

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
