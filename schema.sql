CREATE TABLE IF NOT EXISTS Users (
	user_id	INTEGER PRIMARY KEY AUTOINCREMENT ,
	first_name	TEXT NOT NULL,
	last_name	TEXT,
	phone	INTEGER,
	email	TEXT NOT NULL UNIQUE,
	password	TEXT NOT NULL,
	active INTEGER NOT NULL DEFAULT 1,
	date_created	TEXT,
	hire_date	TEXT,
	user_type	TEXT NOT NULL DEFAULT 'user'
	
);

CREATE TABLE IF NOT EXISTS Assessments (
	assessment_id	INTEGER PRIMARY KEY AUTOINCREMENT ,
	assessment_type	TEXT NOT NULL,
	assessment_description	TEXT NOT NULL,
	creation_date	TEXT,
	due_date	TEXT,
	competency_id	INTEGER,
	FOREIGN KEY(competency_id) REFERENCES Competencies(competency_id)
);

CREATE TABLE IF NOT EXISTS Competencies (
    competency_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    competency_name TEXT NOT NULL UNIQUE,
    creation_date TEXT    
);

CREATE TABLE IF NOT EXISTS AssessmentResults (
	result_id INTEGER PRIMARY KEY AUTOINCREMENT ,
	user_id	INTEGER,
	assessment_id	INTEGER,
	score	INTEGER DEFAULT 0,
	assessment_date	TEXT,
	admin_id	INTEGER,
	FOREIGN KEY(assessment_id) REFERENCES Assessments(assessment_id),
	FOREIGN KEY(user_id) REFERENCES Users(user_id),
	FOREIGN KEY(admin_id) REFERENCES Users(user_id)
);

INSERT INTO Competencies (competency_name, creation_date) VALUES (
	'Computer Anatomy',08082021
);

INSERT INTO Competencies (competency_name, creation_date) VALUES (
    'Data Types',08082021
);
INSERT INTO Competencies (competency_name, creation_date) VALUES (
    'Variables',08082021
);
INSERT INTO Competencies (competency_name, creation_date) VALUES (
    'Functions',08082021
);
INSERT INTO Competencies (competency_name, creation_date) VALUES (
    'Boolean Logic',08082021
);
INSERT INTO Competencies (competency_name, creation_date) VALUES (
    'Conditionals',08082021
);
INSERT INTO Competencies (competency_name, creation_date) VALUES (
    'Loops',08082021
);
INSERT INTO Competencies (competency_name, creation_date) VALUES (
    'Data Structures',08082021
);
INSERT INTO Competencies (competency_name, creation_date) VALUES (
    'Lists',08082021
);
INSERT INTO Competencies (competency_name, creation_date) VALUES (
    'Dictionaries',08082021
);
INSERT INTO Competencies (competency_name, creation_date) VALUES (
    'Working witih Files',08082021
);
INSERT INTO Competencies (competency_name, creation_date) VALUES (
    'Exception Handling',08082021
);
INSERT INTO Competencies (competency_name, creation_date) VALUES (
    'Quality Assurance (QA)',08082021
);
INSERT INTO Competencies (competency_name, creation_date) VALUES (
    'Object-Oriented Programming',08082021
);
INSERT INTO Competencies (competency_name, creation_date) VALUES (
    'Recursion',08082021
);
INSERT INTO Competencies (competency_name, creation_date) VALUES (
    'Databases',08082021
);
INSERT INTO Competencies (competency_name, creation_date) VALUES (
    'Binary Calculator',08082021
);