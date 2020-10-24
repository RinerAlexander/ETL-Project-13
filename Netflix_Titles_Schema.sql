-- Table Schema located here: https://app.quickdatabasediagrams.com/#/d/8H4E5V


CREATE TABLE netflix_titles (
	Show_ID INTEGER PRIMARY KEY,  
	Show_Type VARCHAR(3000) NOT NULL,
	Show_Title VARCHAR(3000),
	Show_Director VARCHAR(3000),
	Show_Cast VARCHAR(3000),
	Show_Country VARCHAR(3000),
	Date_Added DATE,
	Release_Year INTEGER,
	Show_Rating VARCHAR(3000),
	Show_Duration VARCHAR(3000) NOT NULL,
	Listed_In VARCHAR(3000) NOT NULL,
	Show_Description VARCHAR(3000) NOT NULL
);

