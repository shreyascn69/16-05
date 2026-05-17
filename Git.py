-- Create Database
CREATE DATABASE CollegeDB;

-- Use Database
USE CollegeDB;

-- Create Student Table
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    course VARCHAR(50)
);

-- Insert Data
INSERT INTO Students VALUES (1, 'Rahul', 20, 'Male', 'BCA');
INSERT INTO Students VALUES (2, 'Sneha', 21, 'Female', 'BSc');
INSERT INTO Students VALUES (3, 'Arjun', 19, 'Male', 'BCom');

-- View Table
SELECT * FROM Students;

-- Create Teacher Table
CREATE TABLE Teachers (
    teacher_id INT PRIMARY KEY,
    teacher_name VARCHAR(50),
    subject_name VARCHAR(50),
    salary INT
);

-- Insert Teacher Data
INSERT INTO Teachers VALUES (101, 'Ramesh', 'Maths', 50000);
INSERT INTO Teachers VALUES (102, 'Anita', 'Science', 55000);

-- Show Teachers
SELECT * FROM Teachers;

-- Add New Column
ALTER TABLE Students
ADD city VARCHAR(30);

-- Update Data
UPDATE Students
SET city = 'Bangalore'
WHERE student_id = 1;

-- Delete One Row
DELETE FROM Students
WHERE student_id = 3;

-- Display Specific Columns
SELECT name, course FROM Students;
