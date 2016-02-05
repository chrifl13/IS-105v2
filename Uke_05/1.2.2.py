#1.2.2
#a.

import random

#SUIT LIST = ("heart", "spade", "clubs", "diamond")
#NUMERAL LIST = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Knekt", "Dame", "Konge", "ACE")

rank = random.choice(("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "ACE"))
suit = random.choice(("heart", "spade", "clubs", "diamond"))
card = rank + " of " + suit
print(card)
