import re
from dataclasses import dataclass


with open('input.txt', 'r') as infile:
    lines = infile.read().splitlines()
    

@dataclass
class Card:
    number: int
    wins: int
    copies: int = 1

cards = []
for line in lines:
    game, pulls = line.split(':')
    win, have = pulls.split('|')
    win = re.findall(r'\d+', win)
    have = re.findall(r'\d+', have)
    count = len([i for i in win if i in have])
    cards.append(Card(int(re.search(r"\d+", game).group(0)), count))



for card in cards:
    if (wins:= card.wins) > 0:
        for i in range(1, wins + 1):
            cards[card.number - 1 + i].copies += card.copies


print(sum([i.copies for i in cards]))

            