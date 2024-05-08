CREATE DATABASE IF NOT EXISTS web_pages_db;

USE web_pages_db;

CREATE TABLE IF NOT EXISTS web_pages (
    url VARCHAR(255) PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    content TEXT
);
