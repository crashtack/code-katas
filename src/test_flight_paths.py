# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(scope='session')
def cities():
    from flight_paths import import_cities
    cities = import_cities()
    return cities


@pytest.fixture(scope='session')
def nodes():
    from flight_paths import populate_city_nodes
    cities = [{'airport': 'Stockholm-Bromma Airport',
               'destination_airports':
               ["Mohamed Boudiaf Airport",
                "Ain Arnat Airport",
                "Hurghada International Airport"]},
              {'airport': 'Ponciano Arriaga International Airport',
               'destination_airports':
               ["Menorca Airport",
                "Palma de Mallorca Airport",
                "Tenerife South Airport",
                "Frankfurt Airport",
                "Munich Airport"]}
              ]
    return populate_city_nodes(cities)


@pytest.fixture(scope='function')
def edges(nodes):
    from flight_paths import populate_edges
    cities = [{'airport': 'Stockholm-Bromma Airport',
               'destination_airports':
               ["Mohamed Boudiaf Airport",
                "Ain Arnat Airport",
                "Hurghada International Airport"]},
              {'airport': 'Ponciano Arriaga International Airport',
               'destination_airports':
               ["Menorca Airport",
                "Palma de Mallorca Airport",
                "Tenerife South Airport",
                "Frankfurt Airport",
                "Munich Airport"]}
              ]
    # import pdb; pdb.set_trace()
    return populate_edges(nodes, cities)


def test_import_cities():
    '''test that the import json file exists'''
    from flight_paths import import_cities


def test_import_cities_returns_list(cities):
    '''test that import_cities returns a list of city dictionaries'''
    assert type(cities) == list


def test_import_cities_returns_list_of_dicts(cities):
    '''tests that cities is a list of dicts'''
    assert type(cities[0]) == dict


def test_cities_dicts_have_city_key(cities):
    '''tests that the ciiy dict has the key "city"'''
    assert cities[0]['city']


def test_cities_dicts_have_destination_cities_key(cities):
    '''tests that the ciiy dict has the key "destination_cities"'''
    assert cities[0]['destination_cities']


def test_cities_dicts_have_lat_lon(cities):
    '''tests that the ciiy dict has the key "destination_cities"'''
    assert cities[0]['lat_lon']


def test_populate_city_graph_exists():
    '''test that the import for populate_city_nodes works'''
    from flight_paths import populate_city_nodes


def test_city_nodes(nodes):
    '''test that the weighted graph city nodes are beeing populated'''
    # import pdb; pdb.set_trace()
    assert nodes.graph == {'Stockholm-Bromma Airport': {},
                           'Ponciano Arriaga International Airport': {}}


def test_destination_edges_exitsts():
    ''' test that the iport for destination_edges works'''
    from flight_paths import populate_edges


def test_populate_edges_adds_edges(edges):
    '''test populate adds edges to weighted graph'''
    assert edges.graph == {'Stockholm-Bromma Airport': {1: 42, 2: 42},
                           'Ponciano Arriaga International Airport': {1: 42, 2: 42}
                           }












#
