# TODO: open the JSON file
# TODO: import JSON file to a weighted graph
# import json
# import urllib
import requests
from graph import Graph


def calculate_distance(point1, point2):
    """
    Calculate the distance (in miles) between point1 and point2.
    point1 and point2 must have the format [latitude, longitude].
    The return value is a float.

    Modified and converted to Python from:
    http://www.movable-type.co.uk/scripts/latlong.html
    """
    import math

    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3   # km
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])
    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])

    a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1)\
        * math.sin(0.5 * delta_lam)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return radius_earth * c / 1.60934  # convert km to miles


def import_cities():
    '''
        Import the city flight connection path JSON file,
        Returns dictionary of cities
    '''
    # url = '///cities_with_airports.json'
    url = 'https://codefellows.github.io/sea-python-401d4/_downloads/cities_with_airports.json'
    r = requests.get(url)
    cities = r.json()   # converts json to dictionary
    return cities


def populate_city_dict(cities):
    '''Populates a weighted graph with city and conection info'''
    d = {}
    for index, city in enumerate(cities):
        print('index: {} airport: {} lat_lon: {}'
              .format(index, city['airport'], city['lat_lon']))
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
        for destination_airport in city['destination_airports']:
            print('destination_airports: {}'.format(destination_airport))
            # import pdb; pdb.set_trace()
            distance = calculate_distance(cd[airport], cd[destination_airport])
            g.add_edge(airport, destination_airport, distance)

    return g


if __name__ == "__main__":
    # cities = import_cities()
    # g = populate_city_nodes(cities)
    # g = populate_edges(g, cities)
    print('stockholm')
