-- Creates a SQL table with default values on unique id
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
