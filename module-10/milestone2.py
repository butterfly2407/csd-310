# Katie Hilliard, Module 10.1 Assignment, 12/08/2024

import mysql.connector

conn = mysql.connector.connect(
    host='LAPTOP-ED96K4VM',
    user='khilliard24',
    password='Stanle@3!',
    database='milestone2'
)
cursor = conn.cursor()

# Define function to fetch and display data from table
def display_table_data(table_name):
    print(f"\nData from {table_name}")
    cursor.execute(f"SELECT * FROM {table_name}")
    for row in cursor.fetchall():
        print(row)

# List of tables to display data from
tables = [
    "Distributor", "Wine", "`Order`", "Reports", "DistQuarterReport",
    "SalesQuarterReport", "Supplier", "SupplyShipment", "Department",
    "Employee"
]

# Display data for each table
for table in tables:
    display_table_data(table)

# Close connection
cursor.close()
conn.close()

