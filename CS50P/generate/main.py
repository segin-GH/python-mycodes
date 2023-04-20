import random as rnd

# print(rnd.choice (["heads","tails"]))

# print(rnd.randint(1, 10))

cards = ["jack", "queen", "king"]
rnd.shuffle(cards)

for card in cards:
    print(card)
