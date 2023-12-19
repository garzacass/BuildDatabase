# Implementation of Task 3, Q1
import sqlite3

# Function to create summary report
def generate_summary_report():
    # Connect to the SQLite database
    con = sqlite3.connect('notown_records.db')
    cur = con.cursor()

    # Summary report queries
    print("MUSICIANS") #1
    num_musician(cur)
    print("\n\nALBUMS") #2
    num_albums(cur)
    print("\n\nINSTRUMENTS") #3
    num_instruments(cur)
    print("\n\nMUSICIANS AND THEIR ALBUMS") #4
    mus_album(cur)
    # Close the connection
    con.close()

# 1. A total number of musicians and a list of musicians at Notown
def num_musician(cur):
    # total musicians
    statement = 'SELECT COUNT(*) FROM Musician;'
    answer = cur.execute(statement)

    print("Total number of musicians: ",)
    for row in answer:
        print(row)

    # list of musicians
    statement = 'SELECT name, SSN FROM Musician;'
    answer = cur.execute(statement)

    print("----------------")
    attrs = [attr_name[0] for attr_name in answer.description]
    print(attrs)
    print("----------------")
    for row in answer:
        print(row)

# 2. A total number of albums and a list of albums recorded at Notown
def num_albums(cur):
    # total albums
    statement = 'SELECT COUNT(*) FROM Album;'
    answer = cur.execute(statement)

    print("Total number of albums: ")
    for row in answer:
        print(row)

    # list of albums
    statement = 'SELECT id, name, date, type FROM Album;'
    answer = cur.execute(statement)

    print("----------------------------")
    attrs = [attr_name[0] for attr_name in answer.description]
    print(attrs)
    print("----------------------------")
    for row in answer:
        print(row)

# 3. A total number of instruments and a list of instruments at Notown 
def num_instruments(cur):
    # total instruments
    statement = 'SELECT COUNT(*) FROM Instrument;'
    answer = cur.execute(statement)

    print("Total number of instruments: ")
    for row in answer:
        print(row)

    # list of albums
    statement = 'SELECT id, type, key FROM Instrument GROUP BY id, type, key;'
    answer = cur.execute(statement)

    print("----------------------------")
    attrs = [attr_name[0] for attr_name in answer.description]
    print(attrs)
    print("----------------------------")
    for row in answer:
        print(row)

# 4. A table consists of the name of musician and the total number of albums written by them
def mus_album(cur):
    # artists and number of albums they have written
    statement = '''SELECT M.name, COUNT(DISTINCT MA.album_id) AS total_albums_written 
                   FROM Musician M LEFT JOIN MusicianAlbum MA ON M.SSN = MA.SSN
                   GROUP BY M.SSN, M.name;'''
    answer = cur.execute(statement)

    print("----------------------------")
    attrs = [attr_name[0] for attr_name in answer.description]
    print(attrs)
    print("----------------------------")
    for row in answer:
        print(row)


# run summary
if __name__ == "__main__":
    generate_summary_report()

