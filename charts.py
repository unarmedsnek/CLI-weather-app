"""
This module contains functions to create and save charts for weather data about more than one city

Main functions:
- save_comparison_chart(city_temps): Creates and saves a bar chart comparing temperatures of multiple cities.
- save_weather_chart(weather): Creates and saves a bar chart showing the temperature and "feels like" temperature for a single city, with a timestamp in the filename for uniqueness.
"""

import matplotlib.pyplot as plt
import datetime

# This module contains functions to create and save charts for weather data about more than one city
def save_comparison_chart(city_temps):
    """
    Creates and saves a bar chart comparing temperatures of multiple cities.

    :param city_temps: A list of tuples, where each tuple contains a city name and its corresponding temperature (e.g., [('City1', temp1), ('City2', temp2), ...]).
    """

    cities = [str(city) for city, temp in city_temps]
    temps = [float(temp) for city, temp in city_temps]

    plt.bar(cities, temps)
    plt.title('Temperature Comparison Chart')
    plt.xlabel('Cities')
    plt.ylabel('Temperature (°C)')

    timestampNow = datetime.datetime.now().strftime("%y-%m-%d_%H-%M-%S")
    plt.savefig(f'comparisons/comparison_{timestampNow}.png')
    plt.close()

# Does the same thing almost just much simpler and for singular cities
def save_weather_chart(weather):
    """
    Creates and saves a bar chart showing the temperature with a timestamp in the filename for uniqueness.

    :param weather: A dictionary containing weather information for a city, which must include the following
    keys: 'city', 'temp', and 'feels_like'.
    """

    temps = [weather['temp'], weather['feels_like']]
    labels = ['Temp', 'Feels Like']

    plt.bar(labels, temps)
    plt.title(f"Weather in {weather['city']}")
    plt.ylabel("°C")


    timestampNow = datetime.datetime.now().strftime("%y-%m-%d_%H-%M-%S")
    plt.savefig(f'comparisons/weather_{timestampNow}.png')
    plt.close()