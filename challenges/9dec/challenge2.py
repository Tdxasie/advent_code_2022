from operator import add

import matplotlib.pyplot as plt

directions = {
              'L' : (-1, 0),
              'U' : (0, 1),
              'D' : (0, -1),
              'R' : (1, 0),
             }

class Head:
    def __init__(self, pos: tuple):
        self.pos = pos
        self.tail = None
    
    def add_tail(self, tail):
        self.tail = tail

    def move(self, direction: tuple, distance: int) -> list:
        tail_positions = []
        for _ in range(distance):
            self.pos = list(map(add, direction, self.pos))
            tail_pos = self.tail.follow(self.pos)
            tail_positions.append(tail_pos)
        return tail_positions
            
class Tail:
    def __init__(self, head, pos: tuple):
        self.head = head
        self.pos = pos
        self.tail = None
    
    def add_tail(self, tail):
        self.tail = tail
    
    def follow(self, target_pos: tuple):
        # check if target pos close
        # if true dont move
        distx = target_pos[0] - self.pos[0]
        disty = target_pos[1] - self.pos[1]
        
        if abs(distx) <= 1 and abs(disty) <= 1:
            if self.tail:
                return self.tail.follow(self.pos)
        
        distx = distx/abs(distx) if distx != 0 else 0
        disty = disty/abs(disty) if disty != 0 else 0
        
        self.pos = list(map(add, self.pos, (distx, disty)))
        
        if self.tail:
            return self.tail.follow(self.pos)
        
        return tuple(self.pos)

def parse_file(filename):
    with open(filename) as infile:
        lines = infile.read().splitlines()
    return lines


def run_sim(filename):
    lines = parse_file(filename)
    
    head = Head([12,5])
    tail1 = Tail(head, [12,5])
    head.add_tail(tail1)
    
    tails = [tail1]
    
    for i in range(9): # forgotten one tail ffs
        tail = Tail(tails[i], [12,5])
        tails[i].add_tail(tail)
        tails.append(tail)

    tail_positions = []
    
    for line in lines:
        command, distance = line.split(' ')
        distance = int(distance)
        direction = directions[command]
        
        for i in range(distance):
            new_positions = head.move(direction, 1)
        
            positions = [head.pos] + [t.pos for t in tails] + [(12,5)]
            print(positions[0])
            # plt.xlim([0, 26])
            # plt.ylim([0, 20])
            # plt.plot([i[0] for i in positions], [i[1] for i in positions], '*')

            # plt.waitforbuttonpress()
            # plt.clf()
            tail_positions.extend(new_positions)
    
    print(len(set(tail_positions)))
    plt.plot([i[0] for i in tail_positions], [i[1] for i in tail_positions], '*')
    plt.show()
    
if __name__ == '__main__':
    run_sim('9dec/input.txt')