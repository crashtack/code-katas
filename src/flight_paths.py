# TODO: open the JSON file
# TODO: import JSON file to a weighted graph
import json
import urllib
import requests
from graph import Graph


def import_cities():
    '''
        Import the city flight connection path JSON file,
        Returns dictionary of cities
    '''
    url = 'https://codefellows.github.io/sea-python-401d4/_downloads/cities_with_airports.json'
    r = requests.get(url)
    cities = r.json()   # converts json to dictionary
    return cities


def populate_city_weighted_graph(cities):
    '''Populates a weighted graph with city and conection info'''


if __name__ == "__main__":
    for index, item in enumerate(import_cities()):
    # if index == 1:
        if item['city'] == "Kinshasa":
            import pdb; pdb.set_trace()
            for key in item:
                print(key)
                print(item[key])
