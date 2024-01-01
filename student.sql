CREATE TABLE student 
(
	id          BIGINT      	NOT NULL    PRIMARY KEY,
	name        VARCHAR(32) 	NOT NULL,
	enname		VARCHAR(32) 	NOT NULL,
	gender		VARCHAR(8)		NOT NULL,
	dob         DATE       		NOT NULL,
	pob			VARCHAR(128),
	address		VARCHAR(128),
	phone		VARCHAR(16),
	imagepath	VARCHAR(64)
);

CREATE TABLE attendance 
(
	date		DATE			NOT NULL,
	id          BIGINT      	NOT NULL,
	name        VARCHAR(32) 	NOT NULL,
	scantime    TIMESTAMP     	NOT NULL
);

--drop table
drop table student

--drop table
drop table attendance