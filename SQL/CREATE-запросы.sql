CREATE TABLE IF NOT EXISTS genres (
    genre_ID SERIAL PRIMARY KEY,
    genre_name VARCHAR(40) NOT NULL,
    description VARCHAR(1000)
);
	
CREATE TABLE IF NOT EXISTS groups (
    group_ID SERIAL PRIMARY KEY,
    group_name VARCHAR(40) NOT NULL,
    creation_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS albums (
    album_ID SERIAL PRIMARY key,
    album_name VARCHAR(40) NOT NULL,
    creation_date DATE NOT NULL
);
	
CREATE TABLE IF NOT EXISTS tracks (
    track_ID SERIAL PRIMARY KEY,
    track_name VARCHAR(40) NOT NULL,
    duration_in_seconds INTEGER NOT NULL,
    album_ID INTEGER REFERENCES albums(album_ID)
);

CREATE TABLE IF NOT EXISTS collections (
    collection_ID SERIAL PRIMARY KEY,
    collection_name VARCHAR(40) NOT NULL,
    collection_date DATE NOT NULL
);	

CREATE TABLE IF NOT EXISTS group_album (
    group_ID INTEGER REFERENCES groups(group_ID),
    album_ID INTEGER REFERENCES albums(album_ID),
    CONSTRAINT group_album_key PRIMARY key (group_ID, album_ID)
);
	
CREATE TABLE IF NOT EXISTS genre_group (
    genre_ID INTEGER REFERENCES genres(genre_ID),
    group_ID INTEGER REFERENCES groups(group_ID),
    CONSTRAINT genre_group_key PRIMARY key (genre_ID, group_ID)
);

CREATE TABLE IF NOT EXISTS collection_track (
    collection_ID INTEGER REFERENCES collections(collection_ID),
    track_ID INTEGER REFERENCES tracks(track_ID),
    CONSTRAINT collection_track_key PRIMARY key (collection_ID, track_ID)
);
