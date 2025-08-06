CREATE DATABASE CollegeERP;

USE CollegeERP;

CREATE TABLE Students (
    StudentID INT IDENTITY(1,1) PRIMARY KEY,
    FullName NVARCHAR(100) NOT NULL,
    Email NVARCHAR(100) UNIQUE NOT NULL,
    Course NVARCHAR(50),
    EnrollmentDate DATE DEFAULT GETDATE()
);

CREATE TABLE Courses (
    CourseID INT IDENTITY(1,1) PRIMARY KEY,
    CourseName NVARCHAR(100) NOT NULL,
    DurationMonths INT NOT NULL
);

INSERT INTO Courses (CourseName, DurationMonths) VALUES
('Computer Science', 36),
('Information Technology', 36),
('Data Analytics', 12),
('Web Development', 12),
('Artificial Intelligence', 18);

INSERT INTO Students (FullName, Email, Course) VALUES
('Nikita Mathe', 'nikita@example.com', 'Computer Science'),
('Ravi Sharma', 'ravi@example.com', 'Information Technology'),
('Priya Patil', 'priya@example.com', 'Data Analytics'),
('Amit Joshi', 'amit.joshi@example.com', 'Web Development'),
('Sneha Kulkarni', 'sneha.kulkarni@example.com', 'Artificial Intelligence');
