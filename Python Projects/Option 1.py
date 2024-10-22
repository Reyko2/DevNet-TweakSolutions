import requests
import json

# Define mapquest API
MAPQUEST_API_KEY = 'your_mapquest_api_key'
BASE_URL = 'http://www.mapquestapi.com/directions/v2/route'


def get_route(start, end, unit='miles'):
    params = {
        'key': MAPQUEST_API_KEY,
        'from': start,
        'to': end,
        'unit': 'k' if unit == 'metric' else 'm' 
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if data.get('info')['statuscode'] == 0:
        return data['route']
    else:
        return None
