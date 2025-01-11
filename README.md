Weather App

Overview

This Weather App is a simple Python-based application that retrieves and displays real-time weather data using a Weather API. It provides the current temperature and rain percentage for a specified location.

Features
Fetches the current temperature in Celsius or Fahrenheit.
Displays the rain percentage (probability of precipitation).
User-friendly and minimal interface.
Prerequisites
Python: Ensure Python 3.7+ is installed on your system.
API Key: Obtain an API key from a weather data provider (e.g., OpenWeatherMap, WeatherAPI, etc.).
Libraries: Install required Python libraries using the command:
bash
Copy code
pip install requests
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/username/weather-app.git
cd weather-app
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Create a .env file in the project directory and add your API key:
makefile
Copy code
API_KEY=your_api_key_here
Usage
Run the application:
bash
Copy code
python app.py
Enter the location when prompted (e.g., city name or zip code).
View the current temperature and rain percentage in the terminal.
Example Output
yaml
Copy code
Enter your location: London  
Temperature: 18°C  
Rain Percentage: 20%  
Customization
Modify the api_url and query parameters in the app.py file to adjust the API endpoint or add additional features.
Add support for multiple units (Celsius/Fahrenheit) by updating the API query and formatting.
Limitations
Provides only temperature and rain percentage.
Requires a valid API key with sufficient quota.
Dependent on the availability of the Weather API service.
License
This project is licensed under the MIT License.

Contributions
Contributions are welcome! Feel free to submit issues or pull requests to enhance the app.
