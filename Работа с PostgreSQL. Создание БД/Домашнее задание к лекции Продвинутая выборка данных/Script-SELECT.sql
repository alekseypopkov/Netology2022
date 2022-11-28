-- 1. количество исполнителей в каждом жанре;
SELECT name genre, COUNT(g.artists_id) FROM musicgenre m
JOIN genreartists g  ON m.id  = g.musicgenre_id
GROUP BY name;

-- 2.количество треков, вошедших в альбомы 2019-2020 годов;
SELECT COUNT(DISTINCT c.musictrack_id) FROM musictrack m
JOIN collectionmusictrack c ON m.id = c.musictrack_id 
JOIN collection c2 ON c2.id = c.collection_id 
WHERE c2.year_release BETWEEN 2018 AND 2020;

-- 3.средняя продолжительность треков по каждому альбому;
SELECT a.name album,  AVG(m.duration)::time avg_duration FROM album a 
JOIN collectionmusictrack c ON a.id = c.collection_id 
JOIN musictrack m ON m.id = c.musictrack_id
GROUP BY a.name;

-- 4. все исполнители, которые не выпустили альбомы в 2020 году;
SELECT a.name artists, a3.name album, a3.year_release  FROM artists a 
JOIN albumartists a2 ON a.id = a2.artists_id
JOIN album a3 ON a3.id = a2.album_id  
WHERE a3.year_release != 2020
GROUP BY a.name, a3.name, a3.year_release;

-- 5.названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
SELECT c.name collection, m.name track, a4.name artist FROM collection c  
JOIN collectionmusictrack c2  ON c.id = c2.collection_id
JOIN musictrack m ON m.id = c2.musictrack_id 
JOIN album a ON a.id = m.album_id 
JOIN albumartists a2 ON a2.album_id = a.id 
JOIN artists a4 ON a4.id = a2.artists_id 
WHERE a4.name LIKE '%Баста%';

-- 6.название альбомов, в которых присутствуют исполнители более 1 жанра;
SELECT a.name album, COUNT(g.musicgenre_id) count_genre FROM album a 
JOIN albumartists a2 ON a.id = a2.album_id 
JOIN artists a3 ON a3.id = a2.artists_id 
JOIN genreartists g ON g.artists_id = a3.id
JOIN musicgenre m ON m.id = g.musicgenre_id
GROUP BY a.name
HAVING COUNT(g.musicgenre_id) > 1;

-- 7.наименование треков, которые не входят в сборники;
SELECT m.name track, c.collection_id collection FROM musictrack m 
LEFT JOIN collectionmusictrack c ON m.id = c.musictrack_id
WHERE c.collection_id IS NULL;

-- 8. исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);
SELECT a.name artists, m.name track, m.duration FROM artists a
JOIN albumartists a2 ON a.id = a2.artists_id 
JOIN album a3 ON a3.id = a2.album_id 
JOIN musictrack m ON a3.id = m.album_id 
WHERE duration = (SELECT min(duration) FROM musictrack);

-- 9. название альбомов, содержащих наименьшее количество треков.
SELECT id, name album FROM album a 
WHERE id in (SELECT m.album_id FROM musictrack m
GROUP BY album_id 
HAVING COUNT(*) = (SELECT COUNT(*) count FROM musictrack
GROUP BY album_id
ORDER BY count
LIMIT 1));

