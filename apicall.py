import requests

def apidata(link):
    api_link = requests.get(link)
    api_data = api_link.json()
    return api_data