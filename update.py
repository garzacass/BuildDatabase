# Implementation of Task 3, Q2
import argparse
import sqlite3

parser = argparse.ArgumentParser(description='Insert or delete records in the database using command line')
parser.add_argument('--add', help='Add record to the database', action='store_true')
parser.add_argument('--delete', help='Delete record from the database', action='store_true')
parser.add_argument('--table', help='Table name', required=True)
parser.add_argument('--record', help='Record to be added or deleted', required=True)

args = parser.parse_args()
'''
if args.add:
    try:
        con = sqlite3.connect('notown_records.db')
        cur = conn.cursor()
        cur.execute(f"INSERT INTO {args.table} VALUES ({args.record})")
        con.commit()
        con.close()
    except sqlite3.Error as e:
        print("Error adding record:", e)
elif args.delete:
    try:
        con = sqlite3.connect('notown_records.db')
        cur = conn.cursor()
        cur.execute(f"DELETE FROM {args.table} WHERE {args.record}")
        con.commit()
        conn.close()
    except sqlite3.Error as e:
        print("Error adding record:", e)
'''

# Function to add a record
def add_record(table_name, record_values):
    try:
        con = sqlite3.connect('notown_records.db')
        cur = con.cursor()

        # Create the INSERT statement
        insert_statement = f"INSERT INTO {table_name} VALUES ({', '.join(['?']*len(record_values))})"
        cur.execute(insert_statement, record_values)

        con.commit()
        print(f"Record added to {table_name} successfully.")

    except Exception as e:
        print(f"Error adding record to {table_name}: {str(e)}")

    con.close()

# Function to delete a record
def delete_record(table_name, record_values):
    try:
        con = sqlite3.connect('notown_records.db')
        cur = con.cursor()
        
        # Fetch column names from table's schema
        cur.execute(f"PRAGMA table_info({table_name})")
        column_names = [column_info[1] for column_info in cur.fetchall()]

        # Create the DELETE statement with conditions
        condition = ' AND '.join([f"{column}={'?' if not value.isdigit() else value}" for column, value in zip(column_names, record_values)])
        delete_statement = f"DELETE FROM {table_name} WHERE {condition}"
        cur.execute(delete_statement, record_values)

        con.commit()
        print(f"Record deleted from {table_name} successfully.")

    except Exception as e:
        print(f"Error deleting record from {table_name}: {str(e)}")

    con.close()

# parse, add or delete, makes function calls
def command():
    parser = argparse.ArgumentParser(description="Update records in the Notown Records database.")
    parser.add_argument("--add", action="store_true", help="Add a record to the specified table.")
    parser.add_argument("--delete", action="store_true", help="Delete a record from the specified table.")
    parser.add_argument("--table", help="Name of the table.", required=True)
    parser.add_argument("--record", help="Record values (comma-separated).", required=True)

    args = parser.parse_args()

    #add
    if args.add:
        if args.table and args.record:
            add_record(args.table, args.record.split(','))
        else:
            print("Error: Both --table and --record must be specified for the add operation.")
    #delete
    elif args.delete:
        if args.table and args.record:
            delete_record(args.table, args.record.split(','))
        else:
            print("Error: Both --table and --record must be specified for the delete operation.")
    else:
        print("Error: Either --add or --delete must be specified.")


# Run
if __name__ == "__main__":
    command()

