# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(scope='session')
def cities():
    from flight_paths import import_cities
    cities = import_cities()
    return cities


@pytest.fixture(scope='session')
def cd():
    '''returns a dictionary'''
    from flight_paths import populate_city_dict
    cities = [{'airport': 'Stockholm-Bromma Airport',
               'destination_airports':
               ['Uruapan International Airport',
                'Sir Seewoosagur Ramgoolam International Airport'],
               'lat_lon': [59.35444, 17.93972]},
              {'airport': 'Uruapan International Airport',
               'destination_airports':
               ['Stockholm-Bromma Airport',
                'Sir Seewoosagur Ramgoolam International Airport'],
               'lat_lon': [19.39667, -102.03917]},
              {'airport': 'Sir Seewoosagur Ramgoolam International Airport',
               'destination_airports':
               ['Stockholm-Bromma Airport',
                'Uruapan International Airport'],
               'lat_lon': [-20.4300278, 57.6830222]}
              ]
    return populate_city_dict(cities)


@pytest.fixture(scope='function')
def edges(cd):
    from flight_paths import populate_edges
    cities = [{'airport': 'Stockholm-Bromma Airport',
               'destination_airports':
               ['Uruapan International Airport',
                'Sir Seewoosagur Ramgoolam International Airport'],
               'lat_lon': [59.35444, 17.93972]},
              {'airport': 'Uruapan International Airport',
               'destination_airports':
               ['Stockholm-Bromma Airport',
                'Sir Seewoosagur Ramgoolam International Airport'],
               'lat_lon': [19.39667, -102.03917]},
              {'airport': 'Sir Seewoosagur Ramgoolam International Airport',
               'destination_airports':
               ['Stockholm-Bromma Airport',
                'Uruapan International Airport'],
               'lat_lon': [-20.4300278, 57.6830222]}
              ]
    # import pdb; pdb.set_trace()
    return populate_edges(cd, cities)


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
    from flight_paths import populate_city_dict


def test_city_dict(cd):
    '''test that the weighted graph city nodes are beeing populated'''
    # import pdb; pdb.set_trace()
    assert cd == {'Uruapan International Airport': [19.39667, -102.03917],
                 'Stockholm-Bromma Airport': [59.35444, 17.93972]}


def test_destination_edges_exitsts():
    ''' test that the iport for destination_edges works'''
    from flight_paths import populate_edges


def test_populate_edges_adds_edges(edges):
    '''test populate adds edges to weighted graph'''
    import pdb; pdb.set_trace()
    assert edges.graph == {'Stockholm-Bromma Airport':
    {'Uruapan International Airport': 6038.31006865406},
    'Uruapan International Airport':
    {'Stockholm-Bromma Airport': 6038.31006865406}}
