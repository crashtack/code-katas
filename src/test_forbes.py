import pytest


LIST = [
    {'source': 'Microsoft', 'country': 'United States', 'age': 60,
     'net_worth (USD)': 75000000000, 'name': 'Bill Gates', 'rank': 1},
    {'source': 'Zara', 'country': 'Spain', 'age': 80,
     'net_worth (USD)': 67000000000, 'name': 'Amancio Ortega', 'rank': 2},
    {'source': 'Berkshire Hathaway', 'country': 'United States', 'age': 85,
     'net_worth (USD)': 60800000000, 'name': 'Warren Buffett', 'rank': 3}
]


@pytest.fixture
def bd():
    from forbes import populate_dict
    dic = populate_dict(LIST)
    return dic


def test_forbes_import():
    '''testing the import of forbes modual'''
    from forbes import import_data


def test_forbes_returns_list():
    from forbes import import_data
    assert type(import_data()) == list


def test_populate_dict_type():
    import forbes
    assert type(forbes.populate_dict(forbes.import_data())) == dict


def test_populate_dict_value_name(bd):
    assert bd[1]['name'] == 'Bill Gates'


def test_populate_dict_value_age(bd):
    assert bd[1]['age'] == 60


def test_populate_dict_value_net_worth(bd):
    assert bd[1]['net_worth'] == 75000000000


def test_populate_dict_value_net_source(bd):
    assert bd[1]['source'] == 'Microsoft'


def test_populate_dict_value_country(bd):
    assert bd[1]['country'] == 'United States'


def test_populate_dict_value_size(bd):
    # import pdb; pdb.set_trace()
    assert bd.__len__() == 3


def test_populate_bst(bd):
    from forbes import populate_bst
    tree = populate_bst(bd)
    assert tree.size() == 3
