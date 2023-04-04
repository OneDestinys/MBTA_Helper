#Importing our API keys from our 'secure' file
from config import MAPBOX_TOKEN, MBTA_API_KEY
import urllib.request
import json
from pprint import pprint

#Base Urls
MAPBOX_BASE_URL = ""
MBTA_BASE_URL = ""
query = "Babson%20College"
url = f'{MAPBOX_BASE_URL}/query.json?access_token={MAPBOX_TOKEN}&types=poi'
print(url)
def get_mapbox_info(url: str) -> dict:
    """Will take a correctly formatted url and return the dictionary for it"""

def main():
    get_mapbox_info(url)

if __name__ == "__main__":
    main()