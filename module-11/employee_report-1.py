#Amanda New
#Katie Hilliard
#Keanu Foltz
#Amit Rizal

#Module 11
#Milestone 3

#import mysql
import mysql.connector

#establish connection
connection = mysql.connector.connect(
    user='root', #Replace with your user
    password='******', #Replace with your password
    host='127.0.0.1', #Replace with your host
    database='BacchusWine' #Replace with your database name
)

#define employee productivity report
def employee_productivity_report():
    query = """
    SELECT FirstName, LastName AS EmployeeName, Role, (HoursQ1 + HoursQ2 + HoursQ3 + HoursQ4) AS TotalHoursWorked
    FROM Employee
    ORDER BY TotalHoursWorked DESC;
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()

    #print and format results:
    print(f"{'Employee Name':<20} {'Role':<0} {'':<20} {'Annual Total Hours Worked':<0}")
    print("-" * 75)

    for row in results:
        print(f"{row[0]:<5} {row[1]:<15} {row[2]:<25} {row[3]:<1}")

#run function
if __name__ == "__main__":
    try:
        employee_productivity_report()
    finally:
        connection.close()