CREATE TABLE netflix_omdb (
-- 	Columns created by Igor from Netflix csv
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
	Show_Description VARCHAR(3000) NOT NULL,
	
-- 	Columns created by Kaylon from OMdb API
	Awards VARCHAR(1000),
	Genre VARCHAR(1000),
	Language VARCHAR(1000),
	Writer VARCHAR(1000),
	IMDB_ID VARCHAR(15),
	IMDB_Votes VARCHAR(20),
	Rating_IMDB VARCHAR(20),
	Rating_Rotten VARCHAR(20),
	Rating_Metacritic VARCHAR(20)
);

