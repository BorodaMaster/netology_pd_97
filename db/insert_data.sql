-- INSERT artists
INSERT INTO artists(nickname)
VALUES('Rihanna');

INSERT INTO artists(nickname)
VALUES('Gorillaz');

INSERT INTO artists(nickname)
VALUES('Nero Sky');

INSERT INTO artists(nickname)
VALUES('Coldplay');

-- INSERT albums
INSERT INTO albums(name, year)
VALUES('Diamonds', '2017-01-01');

INSERT INTO albums(name, year)
VALUES('Bitch Better', '2018-01-01');

INSERT INTO albums(name, year)
VALUES('Have My Money', '2019-01-01');

INSERT INTO albums(name, year)
VALUES('ANTI', '2020-01-01');
--
-- Diamonds 2017
--  Bitch Better 2018
-- Have My Money 2019
-- ANTI 2020
--

INSERT INTO albums(name, year)
VALUES('Andromeda', '2015-01-01');

INSERT INTO albums(name, year)
VALUES('Saturnz Barz', '2016-01-01');

INSERT INTO albums(name, year)
VALUES('Humanz', '2018-01-01');

INSERT INTO albums(name, year)
VALUES('Garage Palace', '2019-01-01');
--
-- Andromeda 2015
-- Saturnz Barz 2016
-- Humanz 2018
-- Garage Palace 2019
--

INSERT INTO albums(name, year)
VALUES('The Thrill', '2004-01-01');

INSERT INTO albums(name, year)
VALUES('Satisfy', '2005-01-01');

INSERT INTO albums(name, year)
VALUES('Guilt', '2005-01-01');

INSERT INTO albums(name, year)
VALUES('Lullaby', '2020-01-01');
--
-- The Thrill 2004
-- Satisfy 2005
-- Guilt 2019
-- Lullaby 2020
--

INSERT INTO albums(name, year)
VALUES('Hymn for the Weekend', '2012-01-01');

INSERT INTO albums(name, year)
VALUES('Brothers & Sisters', '2014-01-01');

INSERT INTO albums(name, year)
VALUES('Adventure of a Lifetime', '2017-01-01');

INSERT INTO albums(name, year)
VALUES('The Scientist', '2019-01-01');
--
-- Hymn for the Weekend 2012
-- Brothers & Sisters 2014
-- Adventure of a Lifetime 2017
-- The Scientist 2019
--

-- INSERT music_genres
INSERT INTO music_genres(name)
VALUES('Pop');

INSERT INTO music_genres(name)
VALUES('Hip Hop');

INSERT INTO music_genres(name)
VALUES('Reggy');

INSERT INTO music_genres(name)
VALUES('Trip Hop');

INSERT INTO music_genres(name)
VALUES('Rep Rok');

INSERT INTO music_genres(name)
VALUES('Elektro House');

INSERT INTO music_genres(name)
VALUES('Techno');

INSERT INTO music_genres(name)
VALUES('Dabstep');

INSERT INTO music_genres(name)
VALUES('Hard rok');

-- INSERT treks
INSERT INTO treks(name, lenght, album_id)
VALUES('Disturbia', 120, 1);

INSERT INTO treks(name, lenght, album_id)
VALUES('Rude Boy', 120, 1);

INSERT INTO treks(name, lenght, album_id)
VALUES('Take a Bow', 180, 2);

INSERT INTO treks(name, lenght, album_id)
VALUES('Work', 180, 2);

INSERT INTO treks(name, lenght, album_id)
VALUES('Unfaithful', 240, 3);

INSERT INTO treks(name, lenght, album_id)
VALUES('Umbrella', 240, 3);

INSERT INTO treks(name, lenght, album_id)
VALUES('Desperado', 300, 4);
--
-- Diamonds > 1
-- Disturbia
-- Rude Boy
-- Bitch Better > 2
-- Take a Bow
-- Work
-- Have My Money > 3
-- Unfaithful
-- Umbrella
-- ANTI > 4
-- Desperado
--

INSERT INTO treks(name, lenght, album_id)
VALUES('Clint Eastwood', 120, 5);

INSERT INTO treks(name, lenght, album_id)
VALUES('Dare', 120, 5);

INSERT INTO treks(name, lenght, album_id)
VALUES('Humility', 240, 6);

INSERT INTO treks(name, lenght, album_id)
VALUES('Feel good', 240, 6);

INSERT INTO treks(name, lenght, album_id)
VALUES('Dirty Harry', 360, 7);

INSERT INTO treks(name, lenght, album_id)
VALUES('Rock the House', 360, 7);

INSERT INTO treks(name, lenght, album_id)
VALUES('Stylo', 485, 8);
--
-- Andromeda > 5
-- Clint Eastwood
-- Dare
-- Saturnz Barz > 6
-- Humility
-- Feel good
-- Humanz > 7
-- Dirty Harry
-- Rock the House
-- Garage Palace > 8
-- Stylo
--

INSERT INTO treks(name, lenght, album_id)
VALUES('Promises', 180, 9);

INSERT INTO treks(name, lenght, album_id)
VALUES('Me&You', 180, 9);

INSERT INTO treks(name, lenght, album_id)
VALUES('Crushed On You', 240, 10);

INSERT INTO treks(name, lenght, album_id)
VALUES('Guilt', 240, 10);

INSERT INTO treks(name, lenght, album_id)
VALUES('Into the Night', 90, 11);

INSERT INTO treks(name, lenght, album_id)
VALUES('Acts of Mad Men', 90, 11);

INSERT INTO treks(name, lenght, album_id)
VALUES('Innocence', 210, 12);
--
-- The Thrill > 9
-- Promises
-- Me&You
-- Satisfy > 10
-- Crushed On You
-- Guilt
-- Guilt > 11
-- Into the Night
-- Acts of Mad Men
-- Lullaby > 12
-- Innocence
--

INSERT INTO treks(name, lenght, album_id)
VALUES('X BTC', 150, 13);

INSERT INTO treks(name, lenght, album_id)
VALUES('Clocks', 180, 13);

INSERT INTO treks(name, lenght, album_id)
VALUES('Adventure', 250, 14);

INSERT INTO treks(name, lenght, album_id)
VALUES('Yellow', 250, 14);

INSERT INTO treks(name, lenght, album_id)
VALUES('Viva la vida', 100, 15);

INSERT INTO treks(name, lenght, album_id)
VALUES('A sky full of stars', 100, 15);

INSERT INTO treks(name, lenght, album_id)
VALUES('Himn for the Weekend', 485, 16);
--
-- Hymn for the Weekend > 13
-- X BTC
-- Clocks
-- Adventure of a Lifetime > 14
-- Adventure
-- Yellow
-- The Scientist > 15
-- Viva la vida
-- A sky full of stars
-- Brothers & Sisters > 16
-- Himn for the Weekend
--

-- INSERT collections
INSERT INTO collections(name, year)
VALUES('Loud', '2019-01-01');

INSERT INTO collections(name, year)
VALUES('Right Now', '2020-01-01');
--
-- Loud 2019
-- Right Now 2020
--

INSERT INTO collections(name, year)
VALUES('Mix Full Album', '2018-01-01');

INSERT INTO collections(name, year)
VALUES('Compilation', '2019-01-01');
--
-- Mix Full Album 2018
-- Compilation 2019
--

INSERT INTO collections(name, year)
VALUES('End of the World', '2006-01-01');

INSERT INTO collections(name, year)
VALUES('Innocence', '2021-01-01');
--
-- End of the World 2006
-- Innocence 2021
--

INSERT INTO collections(name, year)
VALUES('A Head full of Dreams', '2019-01-01');

INSERT INTO collections(name, year)
VALUES('Talk', '2017-01-01');
--
-- A Head full of Dreams 2019
-- Talk 2017
--

-- INSERT artist_music_genre
INSERT INTO artist_music_genre(artist_id, music_genre_id)
VALUES(1, 1);

INSERT INTO artist_music_genre(artist_id, music_genre_id)
VALUES(1, 2);

INSERT INTO artist_music_genre(artist_id, music_genre_id)
VALUES(1, 3);
--
-- Rihanna > 1
-- Pop > 1
-- Hip Hop > 2
-- Reggy > 3
--

INSERT INTO artist_music_genre(artist_id, music_genre_id)
VALUES(2, 4);

INSERT INTO artist_music_genre(artist_id, music_genre_id)
VALUES(2, 5);

INSERT INTO artist_music_genre(artist_id, music_genre_id)
VALUES(2, 2);
--
-- Gorillaz > 2
-- Trip Hop > 4
-- Rep Rok > 5
-- Hip Hop > 2
--

INSERT INTO artist_music_genre(artist_id, music_genre_id)
VALUES(3, 6);

INSERT INTO artist_music_genre(artist_id, music_genre_id)
VALUES(3, 7);

INSERT INTO artist_music_genre(artist_id, music_genre_id)
VALUES(3, 8);
--
-- Nero Sky > 3
-- Elektro House > 6
-- Techno > 7
-- Dabstep > 8
--

INSERT INTO artist_music_genre(artist_id, music_genre_id)
VALUES(4, 9);
--
-- Coldplay > 4
-- Hard rok > 9
--

-- INSERT artist_album
INSERT INTO artist_album(artist_id, album_id)
VALUES(1, 1);

INSERT INTO artist_album(artist_id, album_id)
VALUES(1, 2);

INSERT INTO artist_album(artist_id, album_id)
VALUES(1, 3);

INSERT INTO artist_album(artist_id, album_id)
VALUES(1, 4);
--
-- Rihanna > 1
-- Diamonds > 1
-- Bitch Better > 2
-- Have My Money > 3
-- ANTI > 4
--

INSERT INTO artist_album(artist_id, album_id)
VALUES(2, 5);

INSERT INTO artist_album(artist_id, album_id)
VALUES(2, 6);

INSERT INTO artist_album(artist_id, album_id)
VALUES(2, 7);

INSERT INTO artist_album(artist_id, album_id)
VALUES(2, 8);
--
-- Gorillaz > 2
-- Andromeda > 5
-- Saturnz Barz > 6
-- Humanz > 7
-- Garage Palace > 8
--

INSERT INTO artist_album(artist_id, album_id)
VALUES(3, 9);

INSERT INTO artist_album(artist_id, album_id)
VALUES(3, 10);

INSERT INTO artist_album(artist_id, album_id)
VALUES(3, 11);

INSERT INTO artist_album(artist_id, album_id)
VALUES(3, 12);
--
-- Nero Sky > 3
-- The Thrill > 9
-- Satisfy > 10
-- Guilt > 11
-- Lullaby > 12
--

INSERT INTO artist_album(artist_id, album_id)
VALUES(4, 13);

INSERT INTO artist_album(artist_id, album_id)
VALUES(4, 14);

INSERT INTO artist_album(artist_id, album_id)
VALUES(4, 15);

INSERT INTO artist_album(artist_id, album_id)
VALUES(4, 16);
--
-- Coldplay > 4
-- Hymn for the Weekend > 13
-- Adventure of a Lifetime > 14
-- The Scientist > 15
-- Brothers & Sisters > 16
--

-- INSERT collection_trek
INSERT INTO collection_trek(collection_id, trek_id)
VALUES(1, 1);

INSERT INTO collection_trek(collection_id, trek_id)
VALUES(1, 3);

INSERT INTO collection_trek(collection_id, trek_id)
VALUES(2, 2);

INSERT INTO collection_trek(collection_id, trek_id)
VALUES(2, 4);
-- 1-7

INSERT INTO collection_trek(collection_id, trek_id)
VALUES(3, 8);

INSERT INTO collection_trek(collection_id, trek_id)
VALUES(3, 10);

INSERT INTO collection_trek(collection_id, trek_id)
VALUES(4, 9);

INSERT INTO collection_trek(collection_id, trek_id)
VALUES(4, 11);
-- 8-14

INSERT INTO collection_trek(collection_id, trek_id)
VALUES(5, 15);

INSERT INTO collection_trek(collection_id, trek_id)
VALUES(5, 17);

INSERT INTO collection_trek(collection_id, trek_id)
VALUES(6, 16);

INSERT INTO collection_trek(collection_id, trek_id)
VALUES(6, 18);
-- 15-21

INSERT INTO collection_trek(collection_id, trek_id)
VALUES(7, 21);

INSERT INTO collection_trek(collection_id, trek_id)
VALUES(7, 23);

INSERT INTO collection_trek(collection_id, trek_id)
VALUES(8, 22);

INSERT INTO collection_trek(collection_id, trek_id)
VALUES(8, 24);
-- 21-28
