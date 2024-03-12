-- 4_first_table.sql

USE `current_database`;

-- Create table first_table if it doesn't exist
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
