# weather
Overview

This project is a FastAPI-based weather application that fetches real-time weather data using the OpenWeatherMap API. The application allows users to enter a city name and receive weather details such as temperature, humidity, and weather description.

What I Learned

Through this project, I learned:

FastAPI: How to build APIs using FastAPI.

API Calling: How to fetch data from third-party APIs using the requests library.

Data Processing: How to extract useful information from a JSON response.

CSV Handling: How to convert API response data into a CSV file.

Project Workflow

Fetch API Response: The application calls the OpenWeatherMap API and retrieves detailed weather data.

Extract Relevant Information: The API returns a large JSON response. I analyzed the response and selected key parameters:

temperature

humidity

weather description

city name

Display Weather Information: The selected data is formatted and displayed to the user.

Save Data to CSV: The full API response is also stored in a CSV file for reference.
