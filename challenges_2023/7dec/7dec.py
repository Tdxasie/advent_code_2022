import re
from dataclasses import dataclass

pips_vals = {
	'2' : 'a',
	'3' : 'b',
	'4' : 'c',
	'5' : 'd',
	'6' : 'e',
	'7' : 'f',
	'8' : 'g',
	'9' : 'h',
	'T' : 'i',
	'J' : 'j',
	'Q' : 'k',
	'K' : 'l',
	'A' : 'm',
}


@dataclass
class Hand:
    hand: str
    bid: int
    type: int = 0
    og_hand: str = ''


def alter_hand(hand: str):
    new_hand = ''
    for char in hand:
        new_hand += pips_vals[char]
    return new_hand
            

with open('input.txt', 'r') as infile:
    lines = infile.read().splitlines()
    
    
hands = []
for line in lines:
    hand, bid = line.split(' ')
    hands.append(Hand(hand, int(bid)))

for hand in hands:
    if len(set(hand.hand)) == 1: #AAAAA
        hand.type = 7
    elif len(set(hand.hand)) == 4: #A23A4
        hand.type = 2
    elif len(set(hand.hand)) == 5: #23456
        hand.type = 1
    else:
        a = sorted([len(re.findall(f'{i}', hand.hand)) for i in set(hand.hand)])
        if a == [1, 4]: #AA8AA
            hand.type = 6
        elif a == [2, 3]: #23332
            hand.type = 5
        elif a == [1, 1, 3]: #TTT98
            hand.type = 4
        elif a == [1, 2, 2]: #23432
            hand.type = 3
    
    hand.og_hand = hand.hand
    hand.hand = alter_hand(hand.hand)

hands = sorted(hands, key= lambda hand: (hand.type, hand.hand))

score = 0
for i, hand in enumerate(hands):
    score += (i+1) * hand.bid

print(hands)

print(score)
        
