# Created by: Emilijus Kanapeckas
"""
This module provides functions to manage the SQLite database for storing weather search history and favorite cities.
It includes functions to initialize the database, save search results, retrieve search history, clear history, and manage favorite cities.

Stored data:
- History: City, Country, Temperature, Feels Like, Humidity, Wind Speed, Description
- Favorites: City

Main functions:
- init_db(): Initializes the database and creates tables if they don't exist.
- save_search(weather): Saves a weather search result to the history table.
- get_last_searches(limit): Retrieves the last N search results from the history table.
- clear_history(): Clears all search history from the history table.
- add_to_favorites(weather): Adds a city to the favorites table.
- remove_from_favorites(city): Removes a city from the favorites table.
- list_favorites(): Retrieves all favorite cities from the favorites table.
- export_history_to_csv(filename): Exports the search history to a CSV file.
"""
import sqlite3
import csv
import ui

def init_db():
    """Initializes the database and creates tables if they don't exist."""

    conn = sqlite3.connect('weather_database.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history(
            City TEXT, 
            Country TEXT,
            Temperature REAL,
            Feels_Like REAL,
            Humidity INTEGER,
            Wind_Speed REAL,
            Description TEXT
            );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS favorites(
            City TEXT UNIQUE
            );
    """)

    conn.commit()
    conn.close()

    import os
    print("DB location:", os.path.abspath("weather_database.db"))

def save_search(weather: dict) -> None:
    """
    Saves a weather search result to the history table.

    :param weather: A dictionary containing weather information for a city, which must include the following
    keys: 'city', 'country', 'temp', 'feels_like', 'humidity', 'wind', and 'description'.
    """
    conn = sqlite3.connect('weather_database.db')
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO history (City, Country, Temperature, Feels_Like, Humidity, Wind_Speed, Description)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        weather['city'],
        weather['country'],
        weather['temp'],
        weather['feels_like'],
        weather['humidity'],
        weather['wind'],
        weather['description']
    ))  # The question marks are placeholders for the values that will be inserted, which helps prevent SQL injection attacks.

    conn.commit()
    conn.close()

def get_last_searches(limit=10) -> list:
    """
    Retrieves the last N search results from the history table.

    :param limit: The number of recent search results to retrieve (default is 10).
    :return: A list of dictionaries containing the search results, ordered from most recent to least
    """
    conn = sqlite3.connect('weather_database.db')
    conn.row_factory = sqlite3.Row  # Enable dictionary-like access to rows (because ui works with dictionaries)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT City, Country, Temperature, Feels_Like, Humidity, Wind_Speed, Description
        FROM history
        ORDER BY rowid DESC
        LIMIT ?
    """, (limit,))

    results = cursor.fetchall()
    conn.close()
    return [dict(row) for row in results]

def clear_history() -> None:
    """Clears all search history from the history table."""

    conn = sqlite3.connect('weather_database.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM history")
    conn.commit()
    conn.close()

def add_to_favorites(weather: dict) -> None:
    """
    Adds a city to the favorites table.

    :param weather: A dictionary containing weather information for a city, which must include the 'city' key.
    """

    conn = sqlite3.connect('weather_database.db')
    cursor = conn.cursor()

    cursor.execute("""
            INSERT INTO favorites (City)
            VALUES (?)
        """, (
        weather['city'],
    ))

    conn.commit()
    conn.close()

def remove_from_favorites(city: str) -> None:
    """
    Removes a city from the favorites table.

    :param city: The name of the city to be removed from favorites.
    """

    conn = sqlite3.connect('weather_database.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM favorites WHERE City = ?", (city,))

    conn.commit()
    conn.close()

def list_favorites():
    """Retrieves all favorite cities from the favorites table."""

    conn = sqlite3.connect('weather_database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT City FROM favorites")

    results = cursor.fetchall()
    conn.close()
    return results

def export_history_to_csv(filename: str) -> None:
    """
    Exports the search history to a CSV file.

    :param filename: The name of the CSV file to which the history will be exported.
    """
    try:
        conn = sqlite3.connect('weather_database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM history")
        rows = cursor.fetchall()

        with open(f'history/{filename}', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['City', 'Country', 'Temperature', 'Feels_Like', 'Humidity', 'Wind_Speed', 'Description'])
            writer.writerows(rows)

        conn.close()

        ui.history_filed_saved()

    except sqlite3.Error as e:
        ui.sql_error(e)

    except OSError as e:
        ui.os_error(e)

    except FileNotFoundError as e:
        ui.file_not_found_error(e)
