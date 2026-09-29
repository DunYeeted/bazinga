import requests
import os
from dotenv import load_dotenv

load_dotenv()
APIKEY = os.environ.get('APIKEY')

"""get_products
Queries the hypixel api for all objects, returning a list of dictionaries with info about each item
"""
def get_items() -> list[dict[str, (str | int | dict[str, str])]] | ConnectionError:
    response = requests.api.get('https://api.hypixel.net/v2/resources/skyblock/items').json()
    if not response['success']:
        return ConnectionError(response['cause'])

    return response['items']

"""get_bazaar_products
Gets all the items listed on the bazaar
"""
def get_bazaar_products() -> dict[str, (str | int | dict[str, str])] | ConnectionError:
    response = requests.api.get('https://api.hypixel.net/v2/skyblock/bazaar').json()
    if not response['success']:
        return ConnectionError(response['cause'])

    return response['products']