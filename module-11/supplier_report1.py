# Keanu Foltz 11.1 12/16/24
# This displays a report on the suppliers

import mysql.connector


def supplier_delivery_report():

    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Hurthiggler808',
            database='BacchusWineryDB'
        )
        cursor = connection.cursor()

        query = """
        SELECT
            DATE_FORMAT(ExpectedDelivery, '%Y-%m') AS Month,
            ss.SupplierID,
            s.SupplierName,
            ROUND(AVG(DATEDIFF(ss.ActualDelivery, ss.ExpectedDelivery)), 2) AS AvgDeliveryGap
        FROM
            SupplyShipment ss
        JOIN
            Supplier s ON ss.SupplierID = s.SupplierID
        GROUP BY
            Month, ss.SupplierID, s.SupplierName
        ORDER BY
            Month, ss.SupplierID;
        """

        cursor.execute(query)
        results = cursor.fetchall()

        print(f"\n{'Month':<10} {'SupplierID':<15} {'SupplierName':<25} {'AvgDeliveryGap':<15}")
        print("-" * 65)

        for row in results:
            print(f"{row[0]:<10} {row[1]:<15} {row[2]:<25} {row[3]:<15}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("\nDatabase connection closed.")


if __name__ == "__main__":
    supplier_delivery_report()