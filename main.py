import os
import apilink as al
import apicall as ac
import printfile as pf

user_api = os.environ['current_weather_data']
location = input('Enter City Name:')

complete_api_link = al.cal(user_api,location)

api_data = ac.apidata(complete_api_link)

pf.printdata(api_data,location)