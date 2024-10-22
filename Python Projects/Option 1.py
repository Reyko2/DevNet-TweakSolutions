import requests
import json

# Define constants for MapQuest API
MAPQUEST_API_KEY = 'your_mapquest_api_key'
BASE_URL = 'http://www.mapquestapi.com/directions/v2/route'

# Function to get route data
def get_route(start, end, unit='miles'):
    params = {
        'key': MAPQUEST_API_KEY,
        'from': start,
        'to': end,
        'unit': 'k' if unit == 'metric' else 'm'  # 'k' for kilometers, 'm' for miles
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if data.get('info')['statuscode'] == 0:
        return data['route']
    else:
        return None

# Function to display route information
def display_route_info(route):
    print("\n--- Route Information ---")
    print(f"Distance: {route['distance']} miles" if route['unit'] == 'm' else f"Distance: {route['distance']} kilometers")
    print(f"Time: {route['formattedTime']}")
    print(f"Fuel Used: {route['fuelUsed']} gallons" if route['unit'] == 'm' else f"Fuel Used: {route['fuelUsed']} liters")
    
    # Display formatted directions
    print("\n--- Directions ---")
    for leg in route['legs'][0]['maneuvers']:
        print(f"{leg['narrative']} ({leg['distance']:.2f} miles)" if route['unit'] == 'm' else f"{leg['narrative']} ({leg['distance']:.2f} kilometers)")

# Main program
if __name__ == '__main__':
    print("Welcome to the MapQuest Route Finder")
    start_location = input("Enter starting location: ")
    end_location = input("Enter destination: ")
    unit_choice = input("Do you prefer metric system (kilometers) or imperial system (miles)? (metric/imperial): ").strip().lower()

    route_data = get_route(start_location, end_location, 'metric' if unit_choice == 'metric' else 'miles')
    if route_data:
        display_route_info(route_data)
    else:
        print("Error: Unable to fetch route information. Please check your inputs or try again later.")
