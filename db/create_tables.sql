CREATE TABLE IF NOT EXISTS artists (
    artist_id SERIAL PRIMARY KEY,
    nickname VARCHAR(128) NOT NULL
);

CREATE TABLE IF NOT EXISTS albums (
    album_id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    year DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS treks (
    trek_id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    lenght SMALLINT NOT NULL,
    album_id SERIAL NOT NULL REFERENCES albums(album_id)
);

CREATE TABLE IF NOT EXISTS music_genres (
    music_genre_id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL
);

CREATE TABLE IF NOT EXISTS collections (
    collection_id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    year DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS artist_album (
    artist_id SERIAL NOT NULL REFERENCES artists(artist_id),
    album_id SERIAL NOT NULL REFERENCES albums(album_id),
    CONSTRAINT PK_artist_album PRIMARY KEY (artist_id, album_id),
    last_update TIMESTAMP
);

CREATE TABLE IF NOT EXISTS artist_music_genre (
    artist_id SERIAL NOT NULL REFERENCES artists(artist_id),
    music_genre_id SERIAL NOT NULL REFERENCES music_genres(music_genre_id),
    CONSTRAINT PK_artist_music_genre PRIMARY KEY (artist_id, music_genre_id),
    last_update TIMESTAMP
);

CREATE TABLE IF NOT EXISTS collection_trek (
    collection_id SERIAL NOT NULL REFERENCES collections(collection_id),
    trek_id SERIAL NOT NULL REFERENCES treks(trek_id),
    CONSTRAINT PK_collection_trek PRIMARY KEY (collection_id, trek_id),
    last_update TIMESTAMP
);
