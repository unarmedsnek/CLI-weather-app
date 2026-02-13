# Weather CLI Application

> A feature-rich command-line weather application that provides real-time weather data, city comparisons, search history, and favorites management.

**Developed by:** Emilijus Kanapeckas & Ahmad Tohme

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Design Decisions](#design-decisions)
- [Technologies Used](#technologies-used)
- [Requirements](#requirements)
- [Contributing](#contributing)

---

## 🌤️ Overview

Weather CLI is a terminal-based application that provides comprehensive weather information using the OpenWeatherMap API. The application features an intuitive menu-driven interface built with Rich for enhanced visual presentation, SQLite database for persistent storage, and Matplotlib for temperature visualization charts.

---

## ✨ Features

- **Single City Weather**: Get detailed weather information for any city worldwide
- **Multi-City Comparison**: Compare temperatures across multiple cities simultaneously
- **Search History**: View your last 5 weather searches
- **Favorites Management**: Save and manage your favorite cities
- **Visual Charts**: Automatically generated temperature comparison charts
- **Data Export**: Export search history to CSV format
- **Persistent Storage**: SQLite database for reliable data persistence

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd weather_cli
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**
   Ensure all dependencies are installed:
   - `requests` - For API communication
   - `rich` - For terminal UI enhancement
   - `matplotlib` - For chart generation

---

## 🚀 How to Run

Execute the main script from the project directory:

```bash
python main.py
```

Upon launching, you'll be greeted with an interactive menu that guides you through all available features.

---

## 💡 Usage

### Main Menu Options

1. **Get weather for a city**
   - Enter a city name to retrieve current weather data
   - Displays temperature, feels-like temperature, humidity, wind speed, and description
   - Automatically saves a chart to the `comparisons/` folder
   - Logs the search in your history

2. **Compare temperatures of multiple cities**
   - Enter multiple city names (comma-separated)
   - View side-by-side comparison in a formatted table
   - Generates a comparative bar chart

3. **View last 5 searches**
   - Quick access to your recent weather queries
   - Data retrieved from local SQLite database

4. **View/Manage favorites**
   - Add cities to your favorites list
   - View all favorited cities
   - Remove cities from favorites
   - Go back to main menu

5. **Export search history to CSV**
   - Export your entire search history to a CSV file
   - Useful for data analysis and record-keeping

6. **Clear search history**
   - Remove all entries from your search history
   - Favorites remain unaffected

7. **Exit**
   - Safely close the application

---

## 📁 Project Structure

```
weather_cli/
│
├── main.py              # Entry point - wires together all modules
├── api.py               # OpenWeatherMap API integration
├── ui.py                # Rich-based terminal UI components
├── db.py                # SQLite database operations
├── charts.py            # Matplotlib chart generation
├── config.py            # Configuration (API keys, endpoints)
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
│
├── weather_database.db  # SQLite database (auto-generated)
├── comparisons/         # Saved weather charts
└── __pycache__/         # Python cache files
```

### Module Responsibilities

- **`main.py`**: Orchestrates the application flow, handles user interaction loop
- **`api.py`**: Handles all HTTP communication with OpenWeatherMap API, data parsing
- **`ui.py`**: Manages all terminal output using Rich library for beautiful formatting
- **`db.py`**: Encapsulates all database operations for search history and favorites
- **`charts.py`**: Generates and saves visual temperature charts using Matplotlib
- **`config.py`**: Centralizes configuration variables for easy maintenance

---

## 🎯 Design Decisions

### Why Rich for UI?

**Rich** was chosen over standard `print()` statements for several reasons:
- **Enhanced Readability**: Colored output and styled text make information easier to parse
- **Professional Appearance**: Panels, tables, and formatted output create a polished user experience
- **Better UX**: Visual hierarchy helps users navigate the application more intuitively
- **Cross-platform**: Works consistently across Windows, macOS, and Linux terminals

### Why SQLite?

**SQLite** was selected as the database solution because:
- **Zero Configuration**: No separate database server required
- **Lightweight**: Single file database, perfect for CLI applications
- **Built-in Support**: Python's `sqlite3` module comes pre-installed
- **Reliability**: ACID-compliant, ensuring data integrity
- **Portability**: Database file can be easily backed up or transferred

### Why Separate Modules?

The project follows **separation of concerns** principle:
- **Maintainability**: Each module has a single, well-defined responsibility
- **Testability**: Individual modules can be tested in isolation
- **Reusability**: Components can be reused in other projects
- **Collaboration**: Multiple developers can work on different modules simultaneously
- **Scalability**: Easy to extend functionality without affecting other parts

### Why Matplotlib for Charts?

**Matplotlib** provides:
- **Simplicity**: Easy to generate bar charts with minimal code
- **File Export**: Saves charts as PNG files for sharing and documentation
- **Customization**: Flexible styling options for professional-looking charts
- **Industry Standard**: Widely used and well-documented library

### API Error Handling

Robust error handling was implemented to:
- Handle network failures gracefully
- Provide clear feedback when cities are not found
- Continue operation even if some cities in a comparison fail
- Prevent application crashes from external API issues

---

## 🛠️ Technologies Used

| Technology | Purpose | Version |
|------------|---------|---------|
| Python | Core programming language | 3.8+ |
| OpenWeatherMap API | Weather data source | 2.5 |
| Rich | Terminal UI enhancement | Latest |
| SQLite | Data persistence | 3.x |
| Matplotlib | Chart generation | Latest |
| Requests | HTTP communication | Latest |

---

## 📋 Requirements

```
requests
rich
matplotlib
```

All dependencies are listed in `requirements.txt` and can be installed with:
```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

This project was developed as a collaborative effort by:
- **Emilijus Kanapeckas**
- **Ahmad Tohme**

### Development Guidelines

- Follow PEP 8 style guidelines for Python code
- Add docstrings to all functions and modules
- Test thoroughly before committing changes
- Update documentation when adding new features

---

## 📝 Notes

- **API Key**: The application uses a hardcoded API key in `config.py`. For production use, consider using environment variables.
- **Rate Limiting**: OpenWeatherMap free tier has request limits. Use responsibly.
- **Charts**: All generated charts are saved in the `comparisons/` directory with timestamps.
- **Database**: The SQLite database (`weather_database.db`) is created automatically on first run.

---

## 📄 License

This project is provided as-is for educational purposes.

---

## 🐛 Troubleshooting

### Common Issues

**Import Errors**
```bash
pip install -r requirements.txt
```

**API Connection Issues**
- Check your internet connection
- Verify the API key in `config.py` is valid
- Check OpenWeatherMap service status

**Database Errors**
- Delete `weather_database.db` and restart the application
- Check file permissions in the project directory

---

**Last Updated**: February 2026
