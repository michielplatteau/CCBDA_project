# from csv to posgres locally
import psycopg2
import csv

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="CCBDA-warinfo",
    user="postgres",
    password="1234"
)

# Open the CSV file
with open('data/interpreted_data_Michiel.csv', 'r') as file:
    csv_data = csv.reader(file)
    next(csv_data)

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Create the table in the database:
    # cursor.execute("CREATE TABLE Kills ( day DATE PRIMARY KEY, losses INTEGER);")

    # Define the INSERT query
    insert_query = f"INSERT INTO war_info_app_equipmentprediction (date,\
    aircraft_lower,\
    aircraft_upper,\
    aircraft)\
    VALUES (%s, %s, %s, %s)"

    data_to_insert = [tuple(row) for row in csv_data]

    # Execute the INSERT query with multiple rows
    cursor.executemany(insert_query, data_to_insert)

    # Commit the changes to the database
    conn.commit()

    # Close the cursor and the database connection
    cursor.close()
    conn.close()
