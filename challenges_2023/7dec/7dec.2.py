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
    'J' : '1',
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
    hand_scheme = sorted([len(re.findall(f'{i}', hand.hand)) for i in set(hand.hand)])
    
    if hand_scheme == [5]: #AAAAA
        hand.type = 7
        
    if hand_scheme == [1, 4]: #AA8AA
        hand.type = 6
        if 'J' in hand.hand : #AAJAA
            hand.type = 7
        
    if hand_scheme == [2, 3]: #23332
        hand.type = 5
        if 'J' in hand.hand: #J333J OR 2JJJ2
            hand.type = 7
        
    if hand_scheme == [1, 1, 3]: #TTT98
        hand.type = 4
        if 'J' in hand.hand: #TTT9J OR TTTJ8 OR JJJ98
            hand.type = 6
        
    if hand_scheme == [1, 2, 2]: #23432
        hand.type = 3
        if 'J' in hand.hand:
            if hand.hand.count('J') == 2: #J343J OR 2J4J2 
                hand.type = 6
            if hand.hand.count('J') == 1: #23J32
                hand.type = 5
        
    if hand_scheme == [1, 1, 1, 2]: #A23A4
        hand.type = 2
        if 'J' in hand.hand: #AJ3A4 OR A2JA4 OR A23AJ OR J23J4
            hand.type = 4
        
    if hand_scheme == [1, 1, 1, 1, 1]: #23456
        hand.type = 1
        if 'J' in hand.hand: #J3456 OR 2J456 OR 23J56 OR 234J6 OR 2345J
            hand.type = 2
        
    hand.og_hand = hand.hand
    hand.hand = alter_hand(hand.hand)

hands = sorted(hands, key= lambda hand: (hand.type, hand.hand))

with open('hands.txt', 'w') as f:
    for hand in hands:
        f.write(str(hand) + '\n')

score = 0
for i, hand in enumerate(hands):
    score += (i+1) * hand.bid

print(hands)

print(score)
        
