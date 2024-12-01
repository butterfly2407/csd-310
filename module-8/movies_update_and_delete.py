# Katie Hilliard, 12/1/2024, Module 8.2 Assignment

import mysql.connector
from mysql.connector import errorcode

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='LAPTOP-ED96K4VM',
            user='khilliard24',
            password='Stanle@3!',
            database='movies'
        )
        return connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None
    
def show_films(cursor, title):
    # Inner join query to get film name, director, genre, and studio
    query = """
        SELECT film_name AS Name,
               film_director AS Director,
               genre_name AS Genre,
               studio_name AS 'Studio Name'
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id
    """
    cursor.execute(query)
    films = cursor.fetchall()

    # Show title
    print("\n-- {} --".format(title))

    # Iterate over the results and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

def insert_film(cursor):
    query = """
        INSERT INTO film (film_name, film_director, genre_id, studio_id, film_releaseDate, film_runtime)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = ("Oculus", "Mike Flanagan", 2, 3, "2014", 104)
    cursor.execute(query, values)

def update_film(cursor):
    query = """
        UPDATE film
        SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror')
        WHERE film_name = 'Alien'
    """
    cursor.execute(query)

def delete_film(cursor):
    query = """
        DELETE FROM film
        WHERE film_name = 'Gladiator'
    """
    cursor.execute(query)

def main():
    connection = connect_to_database()
    if connection is None:
        return
    cursor = connection.cursor()

    try:
        # Show films before changes
        show_films(cursor, "DISPLAYING FILMS")

        # Insert a new film
        insert_film(cursor)
        connection.commit()
        show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

        # Update a film
        update_film(cursor)
        connection.commit()
        show_films(cursor, "DISPLAYING FILMS AFTER UPDATE")

        # Delete a film
        delete_film(cursor)
        connection.commit()
        show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

    except mysql.connector.Error as err:
        print("Error: {}".format(err))

    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    main()
