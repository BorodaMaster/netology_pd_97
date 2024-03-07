-- task 2
-- Название и продолжительность самого длительного трека.
SELECT name
FROM treks
WHERE lenght = (SELECT MAX(lenght) FROM treks)
--
-- Название треков, продолжительность которых не менее 3,5 минут (210 > секунд).
SELECT name, lenght
FROM treks
WHERE lenght > 210
ORDER BY lenght ASC
--
-- Названия сборников, вышедших в период с 2018 по 2020 год включительно.
SELECT name, year
FROM collections
WHERE EXTRACT(YEAR FROM year) BETWEEN 2018 AND 2020
ORDER BY year
--
-- Исполнители, чьё имя состоит из одного слова.
SELECT nickname
FROM artists
WHERE (LENGTH(nickname) - LENGTH(REPLACE(nickname, ' ', '')) + 1) = 1
--
-- Название треков, которые содержат слово «you».
SELECT name
FROM treks
WHERE LOWER(name) LIKE '%you%'
--
-- task 3
-- Количество исполнителей в каждом жанре.
SELECT name as genre_name, count(name) as count_artist
FROM artist_music_genre INNER JOIN music_genres
ON artist_music_genre.music_genre_id = music_genres.music_genre_id
GROUP BY name
ORDER BY count_artist ASC
--
-- Количество треков, вошедших в альбомы 2019–2020 годов.
SELECT count(trek_id) as count_treks
FROM albums INNER JOIN treks
ON albums.album_id = treks.album_id
WHERE EXTRACT(YEAR FROM year) BETWEEN 2019 AND 2020
--
-- Средняя продолжительность треков по каждому альбому.
SELECT albums.name, albums.album_id, ROUND(AVG(lenght), 0) as avg_lenght
FROM albums INNER JOIN treks
ON albums.album_id = treks.album_id
GROUP BY albums.name, albums.album_id
ORDER BY albums.album_id
--
-- Все исполнители, которые не выпустили альбомы в 2020 году.
SELECT nickname, albums.name, year
FROM artist_album
JOIN albums ON artist_album.album_id = albums.album_id
JOIN artists ON artists.artist_id = artist_album.artist_id
WHERE EXTRACT(YEAR FROM year) = 2020
--
-- Названия сборников, в которых присутствует конкретный исполнитель (выберите его сами).

-- task 4
-- Названия альбомов, в которых присутствуют исполнители более чем одного жанра.
SELECT albums.name, music_genres.name, count(music_genres.name)
FROM albums
LEFT JOIN artist_album ON albums.album_id = artist_album.album_id
LEFT JOIN artists ON artist_album.artist_id = artists.artist_id
LEFT JOIN artist_music_genre ON artist_music_genre.music_genre_id = artist_music_genre.music_genre_id
LEFT JOIN music_genres ON music_genres.music_genre_id = artist_music_genre.music_genre_id
GROUP BY albums.name, music_genres.name
ORDER BY albums.name
-- Наименования треков, которые не входят в сборники.
SELECT treks.name
FROM treks
LEFT JOIN collection_trek ON collection_trek.trek_id = treks.trek_id
WHERE collection_id is NULL
--
-- Исполнитель или исполнители, написавшие самый короткий по продолжительности трек, — теоретически таких треков может быть несколько.
-- Названия альбомов, содержащих наименьшее количество треков.
SELECT albums.name, albums.album_id, count(albums.album_id) as count_treks
FROM albums
LEFT JOIN treks ON albums.album_id = treks.album_id
GROUP BY albums.album_id
ORDER BY count_treks
--