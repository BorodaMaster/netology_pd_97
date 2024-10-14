CREATE TABLE IF NOT EXISTS swapi_people (
    id SERIAL PRIMARY KEY,
    birth_year VARCHAR(64) NOT NULL
    eye_color VARCHAR(64) NOT NULL
    gender VARCHAR(64) NOT NULL
    hair_color VARCHAR(64) NOT NULL
    height VARCHAR(64) NOT NULL
    homeworld VARCHAR(64) NOT NULL
    mass VARCHAR(64) NOT NULL
    name VARCHAR(64) NOT NULL
    skin color_VARCHAR(64) NOT NULL
    filmsVARCHAR(256) NOT NULL
    speciesVARCHAR(256) NOT NULL
    starshipsVARCHAR(256) NOT NULL
    vehiclesVARCHAR(256) NOT NULL
);