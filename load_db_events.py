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
with open('data/Ukraine_Black_Sea_2020_2023_Apr28-1 - Sheet1.csv', 'r') as file:
    csv_data = csv.reader(file)
    next(csv_data)

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()


    # Create the table in the database:
    # cursor.execute("CREATE TABLE Kills ( day DATE PRIMARY KEY, losses INTEGER);")

    # Define the INSERT query
    insert_query = "INSERT INTO war_info_app_eventsmap (id, date, type, location, latitude, longitude, notes, fatalities) \
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    # Prepare the data to be inserted as a list of tuples

    def format_entry(entry):
        index = [0, 1, 4, 21, 22, 23, 27, 28]
        new_entry = [entry[i] for i in index]
        split_date = new_entry[1].split('-')
        if split_date[1] == 'January':
            split_date[1] = '01'
        elif split_date[1] == 'February':
            split_date[1] = '02'
        elif split_date[1] == 'March':
            split_date[1] = '03'
        elif split_date[1] == 'April':
            split_date[1] = '04'
        elif split_date[1] == 'May':
            split_date[1] = '05'
        elif split_date[1] == 'June':
            split_date[1] = '06'
        elif split_date[1] == 'July':
            split_date[1] = '07'
        elif split_date[1] == 'August':
            split_date[1] = '08'
        elif split_date[1] == 'September':
            split_date[1] = '09'
        elif split_date[1] == 'October':
            split_date[1] = '10'
        elif split_date[1] == 'November':
            split_date[1] = '11'
        elif split_date[1] == 'December':
            split_date[1] = '12'
        new_entry[1] = '-'.join(split_date)
        return new_entry

    data_to_insert = [tuple(format_entry(row)) for row in csv_data]
    print(len(data_to_insert[1]))
    # Execute the INSERT query with multiple rows
    cursor.executemany(insert_query, data_to_insert)

    # Commit the changes to the database
    conn.commit()

    # Close the cursor and the database connection
    cursor.close()
    conn.close()
