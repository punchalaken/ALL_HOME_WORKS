/*Задание 2*/
	  
 SELECT track_name,  duration_in_seconds
   FROM tracks
  WHERE duration_in_seconds = (
	SELECT MAX(duration_in_seconds)
	FROM tracks);

  SELECT track_name, duration_in_seconds
    FROM tracks
   WHERE duration_in_seconds >= 210
ORDER BY duration_in_seconds DESC;
 
 SELECT collection_name, collection_date
   FROM collections
  WHERE collection_date BETWEEN '2018-01-01' AND '2020-12-31';
 
 SELECT group_name
   FROM groups
  WHERE group_name NOT LIKE '% %';

 SELECT track_name
   FROM tracks
  WHERE STRING_TO_ARRAY(LOWER(track_name), ' ') && ARRAY['my', 'мой'];

    
  
/*Задание 3*/

  SELECT genre_name, COUNT(group_id)
    FROM genre_group g1
    JOIN genres g2 
      ON g1.genre_id = g2.genre_id
GROUP BY g2.genre_id, genre_name;

  SELECT count(track_id)
    FROM tracks t 
    JOIN albums a 
      ON t.album_id = a.album_id
   WHERE creation_date BETWEEN '2019-01-01' 
     AND '2020-12-31';
    
  SELECT a.album_name, AVG(duration_in_seconds)
    FROM tracks t
    JOIN albums a 
      ON t.album_id = a.album_id
GROUP BY a.album_name
ORDER BY AVG

  SELECT group_name
    FROM groups
   WHERE group_name NOT IN (
         SELECT group_name
         FROM groups g
         JOIN group_album ga 
         ON g.group_id = ga.group_id 
         JOIN albums a
         ON ga.album_id = a.album_id
         WHERE a.creation_date BETWEEN '2020-01-01'
         AND '2020-12-31'
  );

  SELECT collection_name, group_name
    FROM collections c 
    JOIN collection_track ct 
      ON c.collection_id = ct.collection_id 
    JOIN tracks t
      ON ct.track_id = t.track_id 
    JOIN group_album ga 
      ON t.album_id = ga.album_id 
    JOIN groups g 
      ON ga.group_id = g.group_id 
GROUP BY collection_name, group_name
  HAVING group_name = 'Linkin Park';   
     
/*Дополнительное задание*/
 
   SELECT DISTINCT album_name
     FROM albums a
     JOIN group_album ga 
       ON a.album_id = ga.album_id
     JOIN groups g
       ON ga.group_id = g.group_id
     JOIN genre_group gg 
       ON ga.group_id = gg.group_id 
 GROUP BY album_name, gg.group_id
   HAVING COUNT(gg.genre_id) > 1;

   SELECT track_name
     FROM tracks t 
LEFT JOIN collection_track ct 
       ON t.track_id = ct.track_id 
    WHERE collection_id IS NULL;
    
SELECT group_name, duration_in_seconds
  FROM groups g
  JOIN group_album ga 
    ON g.group_id = ga.group_id
  JOIN albums a 
    ON ga.album_id = a.album_id 
  JOIN tracks t 
    ON t.album_id = a.album_id 
 WHERE duration_in_seconds = (
       SELECT min(duration_in_seconds)
       FROM tracks);
      
  SELECT a.album_name, COUNT(t.track_id) track_count
    FROM albums a
    JOIN tracks t 
      ON a.album_id = t.album_id
GROUP BY a.album_id, a.album_name
  HAVING COUNT(t.track_id) = (
         SELECT MIN(track_count)
         FROM (SELECT COUNT(track_id) track_count
                 FROM albums a
                 JOIN tracks 
                   ON a.album_id = tracks.album_id
             GROUP BY a.album_id) counts);
 
 
 
		
