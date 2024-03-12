-- List all records with score >= 10 of second_table, displaying score and name, ordered by score (top first)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
