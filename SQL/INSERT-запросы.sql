/*Задание 1*/
INSERT INTO genres (genre_name, description)
     VALUES ('ROCK', 'Rock "n" roll is a popular music genre that combines elements of rhythm and blues (R&B), jazz, and country music with the addition of electric instruments. Originally associated with youth revolt and transgression, the genre is known for energetic performances, catchy melodies, and often insightful lyrics.'),
	    ('Country', 'Country music is an American musical style that incorporates elements of folk, bluegrass, blues, and rural dance music. Music historians trace its origins to the southern Appalachian Mountains in the late 1920s, particularly in eastern Tennessee and southwest Virginia.'),
	    ('Jazz', 'Jazz music is a broad style of music characterized by complex harmony, syncopated rhythms, and a heavy emphasis on improvisation. Black musicians in New Orleans, Louisiana developed the jazz style in the early twentieth century.'),
	    ('Blues', 'Blues is a music genre and musical form which originated in the Deep South of the United States around the 1860s. Blues incorporated spirituals, work songs, field hollers, shouts, chants, and rhymed simple narrative ballads from the African-American culture.');
	
INSERT INTO groups (group_name, creation_date)
     VALUES ('Linkin Park', '1996-01-02'),
	    ('Ray Charles', '1947-04-12'),
	    ('Poco', '1968-06-04'),
	    ('Radio Moscow', '2003-12-11');
	  
INSERT INTO genre_group (genre_id, group_id)
     VALUES ( 1, 1),
	    ( 2, 3),
	    ( 3, 4),
	    ( 4, 2),
	    ( 4, 1);
	  
INSERT INTO albums (album_name, creation_date)
     VALUES ('A Thousand Suns', '2010-09-08'),
	    ('Cantamos', '1974-04-12'),
            ('Brain Cycles', '2009-04-14'),
	    ('new album', '2019-04-14');
	  
INSERT INTO group_album (group_id, album_id)
     VALUES ( 1, 1),
	    ( 1, 4),
	    ( 3, 2),
            ( 4, 3);
	  
INSERT INTO tracks (track_name, duration_in_seconds, album_id)
     VALUES ('The requiem', 121, 1),
	    ('Blackout', 279, 1),
	    ('Sagebrush Serenade', 297, 2),
	    ('Western Waterloo', 239, 2),
	    ('Hold On My', 200, 3),
	    ('Brain Cycles', 204, 3),
	    ('New track1', 264, 4),
	    ('New track2', 238, 4),
	    ('New track2', 500, 1);	   
	  
INSERT INTO collections (collection_name, collection_date)
	 VALUES ('collections1', '2022-01-02'),
		('collections2', '2023-01-23'),
	 	('collections3', '2010-10-10'),
		('collections4', '2015-10-12'),
	  	('collections5', '2018-10-12'),
	   	('collections6', '2020-12-31');

INSERT INTO collection_track (collection_id , track_id)
     VALUES ( 1, 1),
	    ( 1, 2),
	    ( 2, 3),
	    ( 2, 4),
	    ( 3, 5),
	    ( 3, 6);

