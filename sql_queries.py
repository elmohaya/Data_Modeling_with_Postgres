# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

#create the first table named songplays
songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays( 
songplay_id serial NOT NULL,
start_time time NOT NULL,
user_id varchar NOT NULL,
level varchar,
song_id varchar NOT NULL,
artist_id varchar NOT NULL,
session_id varchar NOT NULL,
location varchar,
user_agent text,
PRIMARY KEY (songplay_id))
                            
""")

#create the second table named users
user_table_create = (""" CREATE TABLE IF NOT EXISTS users(
user_id varchar NOT NULL,
first_name text,
last_name text,
gender text,
level varchar,
PRIMARY KEY (user_id))
""")

#creat the third table named songs
song_table_create = (""" CREATE TABLE IF NOT EXISTS songs(
song_id varchar NOT NULL,
title text,
artist_id varchar,
year int,
duration float,
PRIMARY KEY (song_id))
""")

#create the fourth table named artists
artist_table_create = (""" CREATE TABLE IF NOT EXISTS artists(
artist_id varchar NOT NULL,
name text,
location varchar,
latitude float,
longitude float,
PRIMARY KEY (artist_id))
""")

#create the fiveth table named time
time_table_create = (""" CREATE TABLE IF NOT EXISTS time (
start_time time NOT NULL,
hour int,
day int,
week int,
month int,
year int,
weekday int,
PRIMARY KEY (start_time))
""")

# INSERT RECORDS


#Here we insert one row to songplay table
songplay_table_insert = ("""INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

#Here we insert one row to users table
user_table_insert = ("""INSERT INTO users 
(user_id, first_name, last_name, gender, level) 
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO NOTHING
""")

#Here we insert one row to songs table
song_table_insert = ("""INSERT INTO songs
(song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO NOTHING
""")

#Here we insert one row to artists table
artist_table_insert = ("""INSERT INTO artists
(artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING
""")

#Here we insert one row to time table
time_table_insert = ("""INSERT INTO time
(start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS


# this query is to find song_id and artist_id given title or name or duration
song_select = ("""
SELECT s.song_id, a.artist_id
FROM songs s
JOIN artists a
ON s.artist_id = a.artist_id
WHERE title = %s OR name = %s OR duration = %s

""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]