-- List all records with a non-empty name value, displaying score and name, ordered by score (top first)
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
