# Katie Hilliard, Module 11.1 Assignment 12/13/2024

import mysql.connector

def wine_sales_performance():
    """Generate a wine sales performance report."""

    try:
        connection = mysql.connector.connect(
            host='LAPTOP-ED96K4VM',
            user='khilliard24',
            password='Stanle@3!',
            database='milestone2'
        )
        cursor = connection.cursor()

        query = """
        SELECT
            WineName,
            COALESCE(Total_Sales, 0) AS Total_Sales,
            COALESCE(Sales_Goal, 0) AS Sales_Goal,
            (COALESCE(Total_Sales, 0) - COALESCE(Sales_Goal, 0)) AS Goal_Difference
        FROM
            Wine
        ORDER BY
            Goal_Difference DESC;
        """

        cursor.execute(query)
        results = cursor.fetchall()

        print("Raw Results:")
        for row in results:
            print(row)
        
        print(f"{'WineName':<15} {'Total_Sales':<15} {'Sales_Goal':<15} {'Goal_Difference':<15}")
        print("-" * 60)

        for row in results:
            print(f"{row[0]:<15} {row[1]:<15} {row[2]:<15} {row[3]:<15}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    wine_sales_performance()