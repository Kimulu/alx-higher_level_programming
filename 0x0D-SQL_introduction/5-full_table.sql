-- 5-full_table.sql

USE `hbtn_0c_0`;

-- Retrieve table structure
SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_name = 'first_table';
