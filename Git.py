# CREATE DATABASE CollegeDB;

# USE CollegeDB;

# CREATE TABLE Students (
#     student_id INT PRIMARY KEY,
#     name VARCHAR(50),
#     age INT,
#     gender VARCHAR(10),
#     course VARCHAR(50),
#     marks INT
# );

# INSERT INTO Students VALUES (1,'Rahul',20,'Male','BCA',85);

# INSERT INTO Students VALUES (2,'Sneha',21,'Female','BCom',78);

# INSERT INTO Students VALUES (3,'Arjun',19,'Male','BSc',92);

# INSERT INTO Students VALUES (4,'Priya',22,'Female','BCA',88);

# INSERT INTO Students VALUES (5,'Kiran',20,'Male','BBA',67);

# SELECT * FROM Students;

# SELECT name,marks FROM Students;

# SELECT * FROM Students WHERE marks > 80;

# SELECT * FROM Students WHERE gender='Female';

# SELECT * FROM Students ORDER BY marks DESC;

# SELECT COUNT(*) FROM Students;

# SELECT AVG(marks) FROM Students;

# SELECT MAX(marks) FROM Students;

# SELECT MIN(marks) FROM Students;

# UPDATE Students
# SET marks = 90
# WHERE student_id = 2;

# DELETE FROM Students
# WHERE student_id = 5;

# ALTER TABLE Students
# ADD city VARCHAR(50);

# UPDATE Students
# SET city='Bangalore'
# WHERE student_id=1;

# UPDATE Students
# SET city='Mysore'
# WHERE student_id=2;

# UPDATE Students
# SET city='Hubli'
# WHERE student_id=3;

# UPDATE Students
# SET city='Mangalore'
# WHERE student_id=4;

# SELECT * FROM Students;

# CREATE TABLE Teachers (
#     teacher_id INT PRIMARY KEY,
#     teacher_name VARCHAR(50),
#     subject_name VARCHAR(50)
# );

# INSERT INTO Teachers VALUES (101,'Ramesh','Maths');

# INSERT INTO Teachers VALUES (102,'Anita','Science');

# SELECT * FROM Teachers;

# SELECT Students.name, Teachers.subject_name
# FROM Students
# JOIN Teachers
# ON Students.student_id = Teachers.teacher_id;

# CREATE TABLE Fees (
#     fee_id INT PRIMARY KEY,
#     student_id INT,
#     amount INT
# );

# INSERT INTO Fees VALUES (1,1,25000);

# INSERT INTO Fees VALUES (2,2,30000);

# SELECT * FROM Fees;

# SELECT Students.name, Fees.amount
# FROM Students
# JOIN Fees
# ON Students.student_id = Fees.student_id;

# DROP TABLE Fees;

# SHOW TABLES;