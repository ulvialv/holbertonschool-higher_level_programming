-- Lists the number of records with the same score, sorted by count (descending).
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER by number DESC;
