CREATE TABLE IF NOT EXISTS MusicGenre (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) NOT NULL
);

CREATE TABLE IF NOT EXISTS Artists (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) NOT NULL
);

CREATE TABLE IF NOT EXISTS GenreArtists (
	musicgenre_id INTEGER REFERENCES MusicGenre(id),
	artists_id INTEGER REFERENCES Artists(id),
	CONSTRAINT pk PRIMARY KEY (musicgenre_id, artists_id)
);

CREATE TABLE IF NOT EXISTS Album (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	year_release DATE
);

CREATE TABLE IF NOT EXISTS AlbumArtists (
	album_id INTEGER REFERENCES Album(id),
	artists_id INTEGER REFERENCES Artists(id),
	CONSTRAINT alb_art PRIMARY KEY (album_id, artists_id)
);

CREATE TABLE IF NOT EXISTS MusicTrack (
	id SERIAL PRIMARY KEY,
	album_id INTEGER NOT NULL REFERENCES Album(id),
	name VARCHAR(80) NOT null,
	duration TIME
);

CREATE TABLE IF NOT EXISTS Collection (
	id SERIAL PRIMARY KEY,
	musictrack_id INTEGER NOT NULL REFERENCES MusicTrack(id),
	name VARCHAR(80) NOT null,
	year_release DATE
);