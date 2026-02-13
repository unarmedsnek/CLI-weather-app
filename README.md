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
   cd CLI-weather-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**
   
   You need to obtain a free API key from OpenWeatherMap:
   
   a. Visit [OpenWeatherMap API](https://openweathermap.org/api) and sign up for a free account
   
   b. Generate your API key from your account dashboard
   
   c. Copy `config.example.py` to `config.py`:
      ```bash
      copy config.example.py config.py
      ```
   
   d. Open `config.py` and replace `PUT_YOUR_API_KEY_HERE` with your actual API key:
      ```python
      API_KEY = 'your_actual_api_key_here'
      DATABASE_URL = 'https://api.openweathermap.org/data/2.5'
      ```
   
   ⚠️ **Important**: Never commit `config.py` to version control. It's already included in `.gitignore` to protect your API key.

4. **Verify installation**
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
CLI-weather-app/
│
├── main.py                  # Entry point - wires together all modules
├── api.py                   # OpenWeatherMap API integration
├── ui.py                    # Rich-based terminal UI components
├── db.py                    # SQLite database operations
├── charts.py                # Matplotlib chart generation
├── config.example.py        # Configuration template (tracked in Git)
├── config.py                # Your API key configuration (NOT in Git)
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── .gitignore               # Git ignore rules
│
├── weather_database.db      # SQLite database (auto-generated, NOT in Git)
├── comparisons/             # Saved weather charts (NOT in Git)
├── history/                 # Exported CSV files (NOT in Git)
└── __pycache__/             # Python cache files (NOT in Git)
```

### Module Responsibilities

- **`main.py`**: Orchestrates the application flow, handles user interaction loop
- **`api.py`**: Handles all HTTP communication with OpenWeatherMap API, data parsing
- **`ui.py`**: Manages all terminal output using Rich library for beautiful formatting
- **`db.py`**: Encapsulates all database operations for search history and favorites
- **`charts.py`**: Generates and saves visual temperature charts using Matplotlib
- **`config.py`**: Centralizes configuration variables (API key, endpoints) - **You must create this from config.example.py**
- **`config.example.py`**: Template configuration file that's safe to commit to version control

### Files Not Tracked in Git

The following files/directories are excluded via `.gitignore` to protect sensitive data and avoid clutter:
- `config.py` - Contains your personal API key
- `weather_database.db` - Your local search history and favorites
- `comparisons/` - Generated chart images
- `history/` - Exported CSV files
- `__pycache__/` - Python bytecode cache

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

- **API Key**: You must create `config.py` from `config.example.py` and add your own OpenWeatherMap API key. The `config.py` file is excluded from Git to protect your credentials.
- **Rate Limiting**: OpenWeatherMap free tier has request limits (60 calls/minute, 1,000,000 calls/month). Use responsibly.
- **Charts**: All generated charts are saved in the `comparisons/` directory with timestamps.
- **Database**: The SQLite database (`weather_database.db`) is created automatically on first run and stores your search history and favorites locally.

---

## 📄 License

This project is provided as-is for educational purposes.

---

## 🐛 Troubleshooting

### Common Issues

**Missing config.py File**
```bash
copy config.example.py config.py
```
Then edit `config.py` and add your OpenWeatherMap API key.

**Import Errors**
```bash
pip install -r requirements.txt
```

**API Connection Issues**
- Check your internet connection
- Verify the API key in `config.py` is valid and properly formatted
- Ensure you've copied `config.example.py` to `config.py`
- Check OpenWeatherMap service status at https://status.openweathermap.org/

**Database Errors**
- Delete `weather_database.db` and restart the application to create a fresh database
- Check file permissions in the project directory

---

**Last Updated**: February 2026
