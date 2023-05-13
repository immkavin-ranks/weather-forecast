# Python Weather Forecast CLI Tool

This is a command-line interface (CLI) tool built in Python that allows users to retrieve weather data for their current location or any other city of their choice. The tool uses two APIs to retrieve the necessary data: Teleport API to validate user input and get the city's coordinates, and Weatherbit API to retrieve the weather data.

## Features

- Retrieve current weather data for the user's location or any other city of their choice.
- Retrieve a 5-day forecast for the selected city.
- Display weather data in a user-friendly format.

## Requirements

The following dependencies must be installed to run the Python Weather Forecast CLI Tool:

- Python 3.6 or higher
- ***'requests'*** library
- ***'datetime'*** library
- ***'config'*** module (which contains your Weatherbit API key)

## Installation
  1. Clone this repository to your local machine.

  2. Navigate to the project directory.

  3. Install the requests library using pip:
        
          pip install requests

  4. Obtain an API key from Weatherbit.

  5. Create a new file named ***'config.py'*** in the project directory and add the following code, replacing [your-api-key] with your actual API key:
       
          api_key = '[your-api-key]'

  6. Run the ***'weather.py'*** file in your terminal using ***'python3 weather.py'***.

## Usage

When you run the ***'weather.py'*** file, the CLI will prompt you to enter a city name. The tool will then validate your input using the Teleport API. If your input is valid, the tool will retrieve the weather data using the Weatherbit API and display it in a user-friendly format.

If the tool is unable to retrieve weather data, it will display an error message.

## Code Structure

The code is structured into several functions:

### ***'validate_city(city)'***

This function takes a city name as an argument and uses the Teleport API to validate it. The function returns ***'True'*** if the city is valid and ***'False'*** otherwise.
         
### ***'get_city()'***

This function prompts the user to enter a city name and calls ***'validate_city(city)'*** to validate the input. The function will continue to prompt the user until a valid city name is entered.
        
### ***'get_weather(city)'***

This function takes a city name as an argument and uses the Weatherbit API to retrieve the weather data for that city. If the request is successful, the function returns the weather data in JSON format. If the request fails, the function returns ***'None'***.

### ***'print_current_weather(weather_data)'***

This function takes the weather data as an argument and prints the current weather for the selected city.

### ***'print_forecast_weather(weather_data)'***

This function takes the weather data as an argument and prints a 5-day weather forecast for the selected city.

### ***'main()'***

This function is the entry point of the program. It calls ***'get_city()'*** to prompt the user for a city name, calls ***'get_weather(city)'*** to retrieve the weather data for the selected city, and calls ***'print_current_weather(weather_data)'*** and ***'print_forecast_weather(weather_data)'*** to display the weather data.

## Example Output

     Enter your location: New York


     Today is 26/10/2021, and the current weather in New York is Scattered clouds with a temperature of 15.3 °C.

     High: 16.3 °C, Low: 14.7 °C.   

     5-day forecast for New York:                                  

     Date            Day             Description                  Max Temp   Min Temp   

     27/10/2021      Wednesday       Scattered clouds             15.8 °C    11.8 °C    

     28/10/2021      Thursday        Broken clouds                14.4 °C    9.9 °C     

     29/10/2021      Friday          Heavy intensity rain         9.9 °C     6.8 °C     

     30/10/2021      Saturday        Light rain                   9.9 °C     7.1 °C     

     31/10/2021      Sunday          Light rain                   11.6 °C    6.7 °C
         
## License
-> This project is licensed under the MIT License. You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software subject to the conditions in the LICENSE file.
    
    
    MIT License

    Copyright (c) 2023 Kavin

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.


