# Data Modeling with Postgres

- In this project we use Postgres and the star schema to model a database for the songs apllication Sparkify (vertual application).

### Files
- This project constitutes several files, including:

 1- create_tables.py -- used to drop and creat tables at the initial step.
 
 2- etl.ipynb -- a jupyter notebook file to examine inserting some data into the database.
 
 3- etl.py -- this file is an extension of etl.ipynb to insert all the data automatically.
 
 4- README.md -- the current file!
 
 5- sql_queries.py -- here we right all drop, create, and insert queries to be further excuted.
 
 6- test.ipynb -- this file is to test the database after insertion is completed.
 

 ### Tables
 
 - We are creating five tables, one is the fact whereas all the others are dimension tables. Here are the tables:
 
 1- songplays -- the fact table.
 2- songs -- gives details about the song.
 3- users -- includes the users data.
 4- artist -- has the information about artists.
 5- time -- organizes days, months, years, and hours into column for easier readings.
 
