CREATE DATABASE student:
USE student;

 CREATE TABLE students(
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  age INT NOT NULL,
  phone_number VARCHAR(20),
  bio TEXT
 );
