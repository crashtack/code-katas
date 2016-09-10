# -*- coding utf-8 -*-


def sort_cards(cards):
    """Sort shuffled list of cards, sorted by rank.

    >>> sort_cards(['3', '9', 'A', '5', 'T', '8', '2', '4', 'Q', '7', 'J', '6', 'K'])
    ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

    """

    # translating the deck to something that can be sorted
    intab = 'ATJQK'
    outtab = '1abcd'
    trantab = str.maketrans(intab, outtab)
    translated_list = []
    for e in cards:
        translated_list.append(e.translate(trantab))

    # sorting
    sorted_list = sorted(translated_list)

    # transalating deck back to A12345679TJQK values
    sorted_deck = []
    trantab2 = str.maketrans(outtab, intab)
    for e in sorted_list:
        sorted_deck.append(e.translate(trantab2))

    return sorted_deck
