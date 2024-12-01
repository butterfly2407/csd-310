# Katie Hilliard, 12/1/2024, Module 7.2 Assignment

import mysql.connector

db = mysql.connector.connect(
    host='LAPTOP-ED96K4VM',
    user='khilliard24',
    password='Stanle@3!',
    database='movies'
)

cursor = db.cursor()

# Query 1: Fetch all fields from the studio table
print("-- DISPLAYING Studio RECORDS --")
cursor.execute("SELECT * FROM studio")
studios = cursor.fetchall()
for studio in studios:
    print(f"Studio ID: {studio[0]}")
    print(f"Studio Name: {studio[1]}\n")

# Query 2: Fetch all fields from the genre table
print("-- DISPLAYING Genre RECORDS --")
cursor.execute("SELECT * FROM genre")
genres = cursor.fetchall()
for genre in genres:
    print(f"Genre ID: {genre[0]}")
    print(f"Genre Name: {genre[1]}\n")

# Query 3: Fetch the names of films with a runtime less than 120 minutes
print("-- DISPLAYING Short Film RECORDS --")
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
short_films = cursor.fetchall()
for film in short_films:
    print(f"Film Name: {film[0]}")
    print(f'Runtime: {film[1]}\n')

# Query 4: Fetch film names and their directors, sorted by the director's name
print("-- DISPLAYING Director RECORDS in Order --")
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
films_directors = cursor.fetchall()
for film_director in films_directors:
    print(f"Film Name: {film_director[0]}")
    print(f"Director: {film_director[1]}\n")

cursor.close()
db.close()
