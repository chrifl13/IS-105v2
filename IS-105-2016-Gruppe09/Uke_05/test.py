#C

import random
def new_deck():
   
    rs = [rank + suit for rank in "A23456789TJQK" for suit in "CDHS"]
    return rs
def draw_cards(n, cards_list):
   
    random.shuffle(cards_list)
    return [cards_list.pop() for k in range(n)]
# new deck
cards_list = new_deck()
print("New deck = %s cards" % len(cards_list))  
# draw n cards per hand
n = 5
# draw the hands
hand1 = draw_cards(n, cards_list)
hand2 = draw_cards(n, cards_list)
print('-'*40)
# show the 2 hands
print("hand1 = %s" % hand1)
print("hand2 = %s" % hand2)
print('-'*40)
print("New deck = %s cards" % len(cards_list))  
