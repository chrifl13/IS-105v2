# sources/veiledning:
# http://www.openbookproject.net/thinkcs/python/english2e/
# https://github.com/kyledinh/toolkit/blob/master/python/poker.py

import collections
import itertools
import random

TYPE_LISTE = ("Hjerter", "Spar", "Ruter", "Kloever")
VERDIER_LISTE = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Knekt", "Dame", "Konge", "Ess")

class card:
    def __init__(self, numeral, suit):
        self.numeral = numeral
        self.suit = suit
        self.card = self.numeral, self.suit
    def __repr__(self):
        return self.numeral + "-" + self.suit
    #inneholder ulike rangering av verdiene til kortene
class poker_hand():
    def __init__(self, card_list):
        self.card_list = card_list
    def __repr__(self):
        short_desc = "Ingen Like. 1/9 rangering, laveste rangering"
        numeral_dict = collections.defaultdict(int)
        suit_dict = collections.defaultdict(int)
        for my_card in self.card_list:
            numeral_dict[my_card.numeral] += 1
            suit_dict[my_card.suit] += 1
        # Ett par
        if len(numeral_dict) == 4:
            short_desc = "Ett par. 2/9 rangering"
        # To par eller tre like
        elif len(numeral_dict) == 3:
            if 3 in numeral_dict.values():
                short_desc ="Tre like. 4/9 rangering"
            else:
                short_desc ="To par. 3/9 rangering"
        # Fullt hus eller 4 like
        elif len(numeral_dict) == 2:
            if 2 in numeral_dict.values():
                short_desc ="Fullt hus. 7/9 rangering"
            else:
                short_desc ="Fire like. 8/9 rangering"
        else:
            # Flush/straight
            straight, flush = False, False
            if len(suit_dict) == 1:
                flush = True
            min_numeral = min([VERDIER_LISTE.index(x) for x in numeral_dict.keys()])
            max_numeral = max([VERDIER_LISTE.index(x) for x in numeral_dict.keys()])
            if int(max_numeral) - int(min_numeral) == 4:
                straight = True
            low_straight = set(("Ess", "2", "3", "4", "5"))
            if not set(numeral_dict.keys()).difference(low_straight):
                straight = True
            if straight and not flush:
                short_desc ="Straight. 5/9 rangering"
            elif flush and not straight:
                short_desc ="Flush. 6/9 rangering"
            elif flush and  straight:
                short_desc ="Straight flush. 9/9 rangering, topp rank"
        enumeration = "/".join([str(x) for x in self.card_list])
        return "{enumeration} ({short_desc})".format(**locals())

class deck(set):
    def __init__(self):
        for numeral, suit in itertools.product(VERDIER_LISTE, TYPE_LISTE):
            self.add(card(numeral, suit))
    def get_card(self):
        a_card = random.sample(self, 1)[0]
        self.remove(a_card)
        return a_card
    def get_hand(self, number_of_cards=5):
        if number_of_cards == 5:
            return poker_hand([self.get_card() for x in range(number_of_cards)])
        else:
            raise NotImplementedError

for i in range(10):
    print(deck().get_hand())
    