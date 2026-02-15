# Created by: Emilijus Kanapeckas
"""
Terminal UI for the Weather App (Rich-powered).

This module contains presentation-layer helpers: menus, prompts, and formatted
output for weather results and user feedback messages.

Main functions:
- main_meniu(): Displays the main menu options to the user.
- prompt_city(): Prompts the user to enter a city name and returns the input.
- show_weather(weather): Displays the weather information for a single city in a formatted table.
- show_multiple_cities(title, rows): Displays weather information for multiple cities in a formatted table.
- favorite_meniu(): Displays the favorites menu options to the user.
- The rest are either prompts, feedback or error messages.
"""

import rich
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# Initialize a Rich console with forced terminal output and true color support for enhanced visual presentation in the terminal.
console = Console(force_terminal=True, color_system="truecolor")

# Define a constant list of column names for displaying weather data in tables, ensuring consistent formatting across different parts of the application.
COLLUMN_LAYOUT = [
    "City",
    "Country",
    "Temperature (°C)",
    "Feels Like (°C)",
    "Humidity (%)",
    "Wind Speed (m/s)",
    "Description"
]

# This function displays the main meniu options to the user using a Rich panel for enhanced visual appeal.
def main_meniu() -> None:
    """Displays the main menu options to the user using a Rich panel for enhanced visual appeal."""

    console.print(Panel(
        "[bold cyan]1. [/bold cyan]Get weather for a city\n"
        "[bold cyan]2.[/bold cyan] Compare temperatures of multiple cities\n"
        "[bold cyan]3.[/bold cyan] View last 5 searches\n"
        "[bold cyan]4.[/bold cyan] View/Manage favorites\n"
        "[bold cyan]5.[/bold cyan] Export search history to CSV\n"
        "[bold cyan]6.[/bold cyan] Clear search history\n"
        "[bold cyan]7.[/bold cyan] Exit",
        title="[bold magenta]Weather App Menu[/bold magenta]",
        border_style="bright_blue"
    ))


# This function prompts the user to enter a city name and returns the input after stripping any leading or trailing whitespace.
def prompt_city() -> str:
    """
    Prompts the user to enter a city name and returns the input after stripping any leading or trailing whitespace.

    :return: str - The city name entered by the user, with leading and trailing whitespace removed.
    """
    city = console.input("[bold green]Enter a city name:[/bold green] ")
    return city.strip()


# This function takes a dictionary containing weather information for a single city and displays it in a formatted table using the Rich library.
def show_weather(weather: dict) -> None:
    """Displays the weather information for a single city in a formatted table using the Rich library."""

    t = Table(title=f"Weather in {weather['city']}, {weather['country']}", box=rich.box.SQUARE)
    t.add_column("Description", style="cyan")

    if weather['temp'] < 10:
        t.add_column("Temperature (°C)", style="blue")
    elif weather['temp'] < 25:
        t.add_column("Temperature (°C)", style="yellow")
    else:
        t.add_column("Temperature (°C)", style="red")

    t.add_column("Feels Like (°C)", style="cyan")
    t.add_column("Humidity (%)", style="cyan")
    t.add_column("Wind Speed (m/s)", style="cyan")

    t.add_row(
        weather['description'],
        str(weather['temp']),
        str(weather['feels_like']),
        str(weather['humidity']),
        str(weather['wind'])
    )
    console.print(t)

def show_multiple_cities(title: str, rows: list) -> None:
    """Displays weather information for multiple cities in a formatted table using the Rich library."""

    table = Table(title=title , box=rich.box.SQUARE)

    for i in COLLUMN_LAYOUT:
        table.add_column(i, style="cyan")

    for row in rows:
        table.add_row(*[str(row[item]) for item in row])

    console.print(table)

def favorite_meniu() -> None:
    """Displays the favorites menu options to the user using a Rich panel for enhanced visual appeal."""

    console.print(Panel(
        "[bold cyan]1. [/bold cyan]Add a city to favorites\n"
        "[bold cyan]2. [/bold cyan]View Favorites\n"
        "[bold cyan]3.[/bold cyan] Remove a Favorite\n"
        "[bold cyan]4.[/bold cyan] Back to Main Menu",
        title="[bold magenta]Favorites Menu[/bold magenta]",
        border_style="bright_blue"
    ))

""" 
Bellow are the various feedback messages that are displayed to the user in different scenarios, 
such as when a city is not found, when charts are saved successfully, or when an invalid choice is made. 
Each function uses the Rich library to print a formatted message to the console.
"""

def remove_favorite_prompt() -> str:
    city = console.input("[bold red]Enter the city name to remove from favorites:[/bold red] ")
    return city.strip()

def city_not_found() -> None:
    console.print("[bold red]City not found. Please try again.[/bold red]")

def no_valid_cities() -> None:
    console.print("[bold red]No valid cities entered. Please try again.[/bold red]")

def city_not_found_skipping(city: str) -> None:
    console.print(f"[bold red]{city} not found, skipping...[/bold red]")

def charts_saved() -> None:
    console.print("[bold green]Charts saved successfully![/bold green]")

def city_removed_from_favorites(city: str) -> None:
    console.print(f"[bold green]{city} removed from favorites.[/bold green]")

def invalid_choice() -> None:
    console.print("[bold red]Invalid choice. Please try again.[/bold red]")

def exit_message() -> None:
    console.print("[bold magenta]Exiting... Goodbye![/bold magenta]")

def empty_favorites() -> None:
    console.print("[bold yellow]No favorites found. Please add some cities to your favorites.[/bold yellow]")

def api_error() -> None:
    console.print("[bold red]Error fetching data from the API. Please try again later.[/bold red]")

def history_filed_saved() -> None:
    console.print("[bold green]Search history exported successfully![/bold green]")

def prompt_history_filename() -> str:
    filename = console.input("[bold green]Enter a filename for the search history (without extension):[/bold green] ")
    return filename.strip()

def prompt_multiple_cities() -> list:
    cities_input = console.input("[bold green]Enter city names separated by commas:[/bold green] ")
    cities = [city.strip() for city in cities_input.split(",") if city.strip()]
    return cities

def prompt_choice() -> str:
    choice = console.input("[bold green]Enter your choice:[/bold green] ")
    return choice.strip()

def sql_error(error: str) -> None:
    console.print(f"[bold red]Database error: {error}[/bold red]")

def os_error(error: str) -> None:
    console.print(f"[bold red]File system error: {error}[/bold red]")

def file_not_found_error(filename: str) -> None:
    console.print(f"[bold red]File not found: {filename}[/bold red]")