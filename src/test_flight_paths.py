# -*- coding: utf-8 -*-
import pytest


@pytest.fixture(scope='session')
def cities():
    from flight_paths import import_cities
    cities = import_cities()
    return cities


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


#
