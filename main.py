#--------------------------------------------------------------------------------------------------------------------------------------------------#

from requests import get
from datetime import datetime
from config import api_key

#--------------------------------------------------------------------------------------------------------------------------------------------------#

def validate_city(city):
    url = f"https://api.teleport.org/api/cities/?search={city}"
    validate = get(url)
    data = validate.json()

    if data["_embedded"]["city:search-results"]:
        return True
    else:
        return False

#--------------------------------------------------------------------------------------------------------------------------------------------------#

def get_city():
    while True:
        city = input('Enter your location: ')
        if validate_city(city):
            return city
        else:
            print("Invalid city name. Please enter a valid city name.")

#--------------------------------------------------------------------------------------------------------------------------------------------------#

def get_weather(city):
    url = f'https://api.weatherbit.io/v2.0/forecast/daily?city={city}&key={api_key}&units=metric&days=7'
    try:
        response = get(url)
        if response.status_code == 200:
            return response.json()
    except ConnectionError as e:
        print("Connection Error: ", e)
    except Exception as e:
        print("Error: ", e)
    return None
    
#--------------------------------------------------------------------------------------------------------------------------------------------------#

def print_current_weather(weather_data):
    city_name = weather_data['city_name']

    today = datetime.now()
    today_date = today.strftime('%d/%m/%Y')

    temperature = weather_data['data'][0]['temp']
    temperature_min = weather_data['data'][0]["min_temp"]
    temperature_max = weather_data['data'][0]['max_temp']

    description = weather_data['data'][0]['weather']['description']

    print('\n' * 50)                    #    Unicode for °C is  \u00b0C
    
    print(f'\tToday is {today_date}, and the current weather in {city_name} is {description} with a temperature of {temperature:.1f} °C.')
    print(f'\n\tHigh: {temperature_max} °C, Low: {temperature_min} °C.')

#--------------------------------------------------------------------------------------------------------------------------------------------------#

def print_forecast_weather(weather_data):
    city_name = weather_data['city_name']

    print(f'\n\n\t5-day forecast for {city_name}: \n')
    print('\tDate\t\tDay\t\tDescription\t\t\t Max Temp\tMin Temp')

    for i, day in enumerate(weather_data['data'][:5]):
        date = datetime.strptime(day['valid_date'], '%Y-%m-%d')
        forecast_date = date.strftime('%d/%m/%Y')
        day_of_week = date.strftime('%A') if i > 1 else ['Today', 'Tomorrow'][i]
        
        forecast_max_temp = day['max_temp']
        forecast_min_temp = day['min_temp']
        forecast_description = day['weather']['description']

        print(f'\n\t{forecast_date} \t{day_of_week:<10} \t{forecast_description:<24} \t{forecast_max_temp:>5.1f} °C \t{forecast_min_temp:.1f} °C')

    print()

#--------------------------------------------------------------------------------------------------------------------------------------------------#

def main():
    user_city = get_city()
    weather_data = get_weather(user_city)

    if weather_data:
        print_current_weather(weather_data)
        print_forecast_weather(weather_data)
    else:
        print('Sorry, we are unable to display weather data at this time.')

#--------------------------------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    main()

#--------------------------------------------------------------------------------------------------------------------------------------------------#