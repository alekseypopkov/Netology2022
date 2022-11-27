-- SELECT 

-- название и год выхода альбомов, вышедших в 2018 году;
SELECT name, year_release FROM album
WHERE year_release  = 2018;

-- название и продолжительность самого длительного трека;
SELECT name, duration FROM musictrack
ORDER BY duration DESC
LIMIT 1

-- название треков, продолжительность которых не менее 3,5 минуты;
SELECT name  FROM musictrack
WHERE duration >= '0:03:30'

-- названия сборников, вышедших в период с 2018 по 2020 год включительно;
SELECT name, year_release  FROM collection
WHERE year_release BETWEEN 2018 AND 2020 

-- исполнители, чье имя состоит из 1 слова;
SELECT name FROM artists
WHERE name NOT LIKE '% %'

-- название треков, которые содержат слово “мой”/“my”.
SELECT name FROM musictrack
WHERE name LIKE '%мой%' OR "name" LIKE '%my%'