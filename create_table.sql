CREATE DATABASE wishlistDB;

USE wishlistDB;

CREATE TABLE PRODUCTS (
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(100),
    PRACE DOUBLE(10,2),
	URL VARCHAR(255),
	NOTE VARCHAR(255)
)