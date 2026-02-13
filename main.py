# created by Emilijus Kanapeckas, Ahmad Tomeh
"""
Weather App main entry point.

This module wires together the UI, API client, chart generation, and database layer.
It initializes the database and runs the interactive menu loop.

Modules:
- ui: Rich-based menus, prompts, formatted tables/messages
- api: OpenWeatherMap data fetching
- charts: chart creation/saving
- db: search history + favorites persistence (SQLite)
"""
import ui
import charts
import api
import db
from ui import show_multiple_cities, prompt_multiple_cities

db.init_db()
ui.main_meniu()

while True:
    choice = ui.prompt_choice()

    # Single city weather menu loop
    if choice == '1':

        city = ui.prompt_city()
        weather_data = api.get_weather(city)
        # Handle city not found
        if weather_data is None:
            ui.city_not_found()
            continue
        # Display weather data, save chart and log search
        ui.show_weather(weather_data)
        charts.save_weather_chart(weather_data)
        db.save_search(weather_data)
        ui.charts_saved()

        print("\n")
        ui.main_meniu()

    # Multiple cities comparison menu loop
    elif choice == '2':
        city_input = prompt_multiple_cities()

        # Get weather data for each city and store valid results
        pairs = []
        pairs_full = []
        for city in city_input:
            weather = api.get_weather(city.strip())
            if weather is None:
                ui.city_not_found_skipping(city.strip())
                continue
            db.save_search(weather)
            pairs.append((weather['city'], weather['temp']))
            pairs_full.append(weather)
            if not pairs:
                ui.no_valid_cities()
                continue

        # print("pairs: ", pairs, "\n")
        # print("pairs_full: ", pairs_full, "\n")
        ui.show_multiple_cities("Multiple City Comparison", pairs_full)
        # Generate and save comparison chart
        charts.save_comparison_chart(pairs)
        ui.charts_saved()

        print("\n")
        ui.main_meniu()

    # Last searches menu loop
    elif choice == '3':
        last_searches = db.get_last_searches(5)
        show_multiple_cities("Last Searches", last_searches)

        print("\n")
        ui.main_meniu()

    # Favorites menu loop
    elif choice == '4':
        ui.favorite_meniu()

        # This loop handles the favorites menu until the user chooses to go back to the main menu
        while True:
            fav_choice = input()

            # Adds a city to favorites
            if fav_choice == '1':
                city = ui.prompt_city()
                weather = api.get_weather(city)
                favorites = db.add_to_favorites(weather)
                print('Added to favorites:', weather['city'])

                print("\n")
                ui.favorite_meniu()

            # Shows all favorited cities
            if fav_choice == '2':
                favorites = db.list_favorites()

                all_favorites = []
                for city in favorites:
                    weather = api.get_weather(city[0].strip())
                    if weather is None:
                        ui.city_not_found_skipping(city.strip())
                        continue
                    all_favorites.append(weather)
                    if not favorites:
                        ui.empty_favorites()
                        continue

                ui.show_multiple_cities("Favorites", all_favorites)

                print("\n")
                ui.favorite_meniu()

            # Removes a city from favorites
            elif fav_choice == '3':
                city_to_remove = ui.remove_favorite_prompt()
                db.remove_from_favorites(city_to_remove)
                ui.city_removed_from_favorites(city_to_remove)

                print("\n")
                ui.favorite_meniu()

            # Goes back to the main menu
            elif fav_choice == '4':
                ui.main_meniu()
                break

            else:
                ui.invalid_choice()

        print("\n")
        ui.main_meniu()

    elif choice == '5':
        # Exports search history to a CSV file for a specified city
        export_filename = ui.prompt_history_filename()
        db.export_history_to_csv(export_filename)
        ui.history_filed_saved()

        ui.main_meniu()

    elif choice == '6':
        # Clears all search history from the database
        db.clear_history()
        ui.history_filed_saved()

        ui.main_meniu()

    # Exits the program
    elif choice == '7':
        ui.exit_message()
        break