# Imports
import sqlite3
import csv

# Connect to database
con = sqlite3.connect('notown_records.db') #create database
cur = con.cursor()

# Function to create tables
def create_tables():
    #musician
    statement = '''
        CREATE TABLE Musician(
            num INTEGER, 
            street TEXT,
            str_type TEXT, 
            name TEXT,
            SSN INTEGER,
            PRIMARY KEY(SSN)
            );'''
    cur.execute(statement)

    #instrument
    statement = '''
        CREATE TABLE Instrument(
            id INTEGER, 
            type TEXT,
            key TEXT, 
            PRIMARY KEY(id)
            );'''
    cur.execute(statement)

    #album
    statement = '''
        CREATE TABLE Album(
            name TEXT,
            id INTEGER, 
            date INTEGER,
            type TEXT, 
            PRIMARY KEY(id)
            );'''
    cur.execute(statement)

    #musician-album
    statement = '''
        CREATE TABLE MusicianAlbum(
            SSN INTEGER,
            album_id INTEGER, 
            PRIMARY KEY(SSN, album_id),
            FOREIGN KEY (album_id) REFERENCES Album(album_id),
            FOREIGN KEY (SSN) REFERENCES Musician(SSN)
            );'''
    cur.execute(statement)

    #album-instrument
    statement = '''
        CREATE TABLE AlbumInstrument(
            album_id INTEGER,
            instrument_id INTEGER, 
            PRIMARY KEY(album_id, instrument_id),
            FOREIGN KEY (album_id) REFERENCES Album(album_id),
            FOREIGN KEY (instrument_id) REFERENCES Instrument(instrument_id)
            );'''
    cur.execute(statement)

# Function to import data
def import_data():
    # file names
    files = ['AlbumInstrument.csv', 'Album.csv', 'Instrument.csv', 'MusicianAlbum.csv', 'Musician.csv']

    # Import the data from the csv files into the database
    for file in files:
        table = file.split('.')[0] #get table name (exclude the .csv part)

        with open(file, 'r') as files:
            csv_reader = csv.reader(files)
            headers = next(csv_reader)

            # Insert statement template
            statement = f"INSERT INTO {table} ({', '.join(headers)}) VALUES ({', '.join(['?']*len(headers))})"

            # Read and insert data into the table
            for row in csv_reader:
                cur.execute(statement, row)

################################################
# Implementation of Tasks 1 and 2
create_tables()
import_data()

# Commit changes and close connection
con.commit()
con.close()

