import sqlite3
from sqlite3 import Error


def create_connection():

    database = r"A:\System.Data.SQLite\2015\bin\vorratskammer.db"

    try:
        connection = sqlite3.connect(database)
        return connection
    except Error as e:
        print(e)


# Creating table
def create_table_query():

    connection = create_connection()
    cursor = connection.cursor()

    sqlite_create_table_query = """CREATE TABLE IF NOT EXISTS Kammer(
                                ArtikelID INTEGER PRIMARY KEY AUTOINCREMENT,
                                ArtikelName TEXT NOT NULL UNIQUE,
                                ArtikelMenge REAL NOT NULL ,
                                Ablaufdatum TEXT);"""

    cursor.execute(sqlite_create_table_query)
    connection.commit()
    print("Tabelle wurde erzeugt!")

    connection.close()


# Insert Values into the table
def insert_into_query(arikel_name, artikel_menge, artikel_ablaufdatum):

    connection = create_connection()
    cursor = connection.cursor()

    artikel = (arikel_name, artikel_menge, artikel_ablaufdatum)

    cursor.execute("INSERT INTO Kammer VALUES(NULL, ?, ?, ?);", artikel)
    connection.commit()

    print(arikel_name, "wurde hinzugefügt.")

    connection.close()


def delete_article_query(artikel_id):

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM Kammer WHERE ArtikelID=:id", {"id": artikel_id})
    connection.commit()

    print("Erfolgreich entfernt.")

    connection.close()


# Select an article by its id
def select_one_by_id_query(artikel_id):

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM Kammer WHERE ArtikelID=:id", {"id": artikel_id})

    all_results = cursor.fetchall()
    print(all_results)

    connection.close()


# Select an article by its name
def select_one_by_name_query(arikel_name):

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM Kammer WHERE ArtikelName=:name", {"name": arikel_name})

    all_results = cursor.fetchall()
    print(all_results)

    connection.close()


# Select an article by its amount
def select_one_by_amount_query(artikel_menge):

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM Kammer WHERE ArtikelMenge=:menge", {"menge": artikel_menge})

    all_results = cursor.fetchall()
    print(all_results)

    connection.close()


# Select an article by its date
def select_one_by_date_query(artikel_ablaufdatum):

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM Kammer WHERE Ablaufdatum=:datum", {"datum": artikel_ablaufdatum})

    all_results = cursor.fetchall()
    print(all_results)

    connection.close()


# Select all articles from the table
def select_all_query():

    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Kammer;")
    all_results = cursor.fetchall()
    print(all_results)

    connection.close()
