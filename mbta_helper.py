#Importing our API keys from our 'secure' file
from config import MAPBOX_TOKEN, MBTA_API_KEY
import urllib.request
import json
from pprint import pprint

#Base Urls
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"



def query_input_mapbox(query):
    """Takes the query and builds the URL for mapbox"""
    #ChatGPT told me how to replace spaces with %20
    query = query.replace(" ","%20")
    url = f'{MAPBOX_BASE_URL}/{query}.json?types=address&access_token={MAPBOX_TOKEN}&types=poi'
    return url

def get_mapbox_info(url: str) -> dict:
    """Will take a correctly formatted url and return the dictionary for it"""
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data

def get_lat_long(response_data: dict) -> tuple[str, str]:
    """Taking the data from the dictionary, this function will return """
    lat_long = []
    #To unreverse the latitude longitude the dict has it in automatically
    lat_long = (response_data['features'][0]['geometry']['coordinates'][-1]), (response_data['features'][0]['geometry']['coordinates'][0])
    lat_long = tuple(lat_long)
    return lat_long

def mbta_stop_finder(lat_long) -> tuple[str, bool]:
    """Takes the lat and long, builds the mbta url, finds the closest mbta station and whether that station is wheelchair accessible"""
    mbta_url = f'https://api-v3.mbta.com/stops?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={lat_long[0]}&filter%5Blongitude%5D={lat_long[1]}'
    print(mbta_url)
    f = urllib.request.urlopen(mbta_url)
    response_text_mbta = f.read().decode('utf-8')
    response_data_mbta = json.loads(response_text_mbta)
    # pprint(response_data_mbta)
    station_name = response_data_mbta["data"][0]['attributes']['name']
    wheel_chair_accessible = bool(response_data_mbta["data"][0]['attributes']['wheelchair_boarding'])
    name_and_wheel = []
    name_and_wheel = (station_name, wheel_chair_accessible)
    name_and_wheel = tuple(name_and_wheel)
    # pprint(name_and_wheel)
    return name_and_wheel

def find_stop_near(address):
    url = query_input_mapbox(address)
    response_data = get_mapbox_info(url)
    lat_long = get_lat_long(response_data)
    closest_stop = mbta_stop_finder(lat_long)
    return closest_stop

if __name__ == "__main__":
    find_stop_near()