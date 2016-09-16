import requests
from graph import Graph
from distance import calculate_distance
import sys
import os
from io import open
import json

def import_cities():
    '''
        Import the city flight connection path JSON file,
        Returns dictionary of cities
    '''
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    filename = 'cities_with_airports.json'
    path = os.path.join(BASE_DIR, filename)
    print('path: {}'.format(path))
    # url = 'https://codefellows.github.io/sea-python-401d4/_downloads/cities_with_airports.json'
    # r = requests.get(url)

    with open(path, 'r') as fh:
        data = fh.read()

    cities = json.loads(data)   # converts json to dictionary
    return cities


def populate_city_dict(cities):
    '''Populates a weighted graph with city and conection info'''
    d = {}
    for index, city in enumerate(cities):
        # print('index: {} airport: {} lat_lon: {}'
            #   .format(index, city['airport'], city['lat_lon']))
        try:
            d.setdefault(city['airport'], city['lat_lon'])

        except ValueError:
            print('\n\nindex: {} airport: {}'.format(index, city['airport']))
            print('VALUE_ERROR\n\n')
            pass
            # import pdb; pdb.set_trace()
    # print(g.nodes())
    return d


def populate_edges(cd, cities):
    '''Add weighted edges(destination_airports, distance) to the
       graph for each node(airport)'''
    g = Graph()
    for index, city in enumerate(cities):
        airport = city['airport']
        for index2, dest_airport in enumerate(city['destination_airports']):

            # import pdb; pdb.set_trace()
            try:
                distance = calculate_distance(cd[airport],
                                              cd[dest_airport])
                # print('Index: {} Airport: {} Destination_airports:'
                    #   ' {} Distance: {}'
                    #   .format(city['airport'], index, dest_airport, distance))
                g.add_edge(airport, dest_airport, distance)
            except KeyError:
                pass

    return g


if __name__ == "__main__":
    start_city = sys.argv[1]
    dest_city = sys.argv[2]
    # print('sys.argv {}'.format(sys.argv))
    # start_city = 'Seattle'
    # dest_city = 'Perth'

    cities = import_cities()
    cd = populate_city_dict(cities)
    g = populate_edges(cd, cities)

    start_airport = None
    dest_airport = None
    for node in g:
        if start_city in node:
            start_airport = node
        if start_airport is None:
            raise NameError("Starting City not found")

        if dest_city in node:
            dest_airport = node
        if dest_airport is None:
            raise NameError("Destination City not found")

        print(g.shortest_path(start_airport, dest_airport))
        print('City not found')
