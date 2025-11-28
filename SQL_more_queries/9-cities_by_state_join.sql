-- Lists all cities with their corresponding state name
-- Each record: cities.id - cities.name - states.name
-- Results are sorted by cities.id in ascending order
-- Database name will be passed as argument to mysql command

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
