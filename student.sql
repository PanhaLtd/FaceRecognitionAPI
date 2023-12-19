CREATE TABLE student 
(
	id          BIGINT      NOT NULL    PRIMARY KEY,
	name        VARCHAR(32) NOT NULL,
	dob         DATE        NOT NULL,
	image_path VARCHAR(64)
);