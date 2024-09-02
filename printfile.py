from datetime import datetime
import createdata as cd
def printdata(api_data,location):
    if api_data['cod'] == '404':
        print('Invalid City: {}, Please check your City name'.format(location))
    else:
        temp_city = ((api_data['main']['temp']) - 273.15)
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_spd = api_data['wind']['speed']
        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        print("-------------------------------------------------------------")
        print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
        print("-------------------------------------------------------------")

        print("Current temperature is: {:.2f} deg C".format(temp_city))
        print("Current weather desc  :", weather_desc)
        print("Current Humidity      :", hmdt, '%')
        print("Current wind speed    :", wind_spd, 'kmph')

        temp_city = round(temp_city,2)
        cd.loaddata(location.upper(), temp_city, weather_desc, hmdt, wind_spd, date_time)