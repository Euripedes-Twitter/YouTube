-- Database: youtube

-- DROP DATABASE youtube;

CREATE DATABASE youtube
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_Ireland.1252'
    LC_CTYPE = 'English_Ireland.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

COMMENT ON DATABASE youtube
    IS 'DataBase created for the Twitter Assignment on 07/05/2021'; 