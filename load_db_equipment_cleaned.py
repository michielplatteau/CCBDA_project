# from csv to posgres locally
import psycopg2
import csv

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="CCBDA-warinfo",
    user="postgres",
    password="012345"
)

# Open the CSV file
with open('data/cleaned_data_equip.csv', 'r') as file:
    csv_data = csv.reader(file)
    next(csv_data)

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Create the table in the database:
    # cursor.execute("CREATE TABLE Kills ( day DATE PRIMARY KEY, losses INTEGER);")

    # Define the INSERT query
    insert_query = f"INSERT INTO war_info_app_equipment (date,\
    day,\
    aircraft,\
    helicopter,\
    tank,\
    apc,\
    field_artillery,\
    mrl,\
    military_auto,\
    fuel_tank,\
    drone,\
    naval_ship,\
    anti_aircraft_warfare,\
    special_equipment,\
    mobile_srbm_system,\
    greatest_losses_direction,\
    vehicles_and_fuel_tanks,\
    cruise_missiles,\
    total_air_units,\
    total_naval_units,\
    total_ground_units) \
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    # Prepare the data to be inserted as a list of tuples

    def format_entry(entry):
        for i, element in enumerate(entry):
            if element[-2:] == ".0":
                entry[i] = element[:-2]

        # greatest losses direc
        return entry

    data_to_insert = [tuple(format_entry(row)) for row in csv_data]

    # Execute the INSERT query with multiple rows
    cursor.executemany(insert_query, data_to_insert)

    # Commit the changes to the database
    conn.commit()

    # Close the cursor and the database connection
    cursor.close()
    conn.close()
