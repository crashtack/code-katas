import os
from bst import BST
import json
from io import open


def import_data():
    '''
        importing the data from file,
        returns a dictionary of billionaires
    '''
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    filename = 'forbes_billionaires_2016.json'
    path = os.path.join(BASE_DIR, filename)
    with open(path, 'r') as fh:
        data = fh.read()

    billionaires = json.loads(data)
    return billionaires


def populate_dict(bils):
    ''' put the list of billionares into a dictianary'''
    dic = {}
    for bil in bils:
        dic.setdefault(bil['rank'], {'name': bil['name'],
                                     'age': bil['age'],
                                     'net_worth': bil['net_worth (USD)'],
                                     'source': bil['source'],
                                     'country': bil['country']
                                     }
                       )
    return dic


def populate_bst(dic):
    '''Takes a dictioanry and populates a wieghted graph with the values'''
    tree = BST()
    for bil in dic:
        # import pdb; pdb.set_trace()
        print(bil, end=', ')
        tree.insert(bil, dic[bil])
    return tree


def return_oldest(bst):
    '''return the oldest billinare under 80 and the youngest'''
    pass


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('hello world')
    elif sys.argv[1] == '--help':
        print('this is your helper string')
    else:
        data = import_data()
        dic = populate_dict(data)
        bst = populate_bst(dic)
