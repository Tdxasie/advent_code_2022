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
    
    head = Head([0, 0])
    tail1 = Tail(head, [0,0])
    head.add_tail(tail1)
    
    tails = [tail1]
    
    for i in range(8):
        tail = Tail(tails[i], [0,0])
        tails[i].add_tail(tail)
        tails.append(tail)

    tail_positions = []
    
    for line in lines:
        command, distance = line.split(' ')
        distance = int(distance)
        direction = directions[command]
        
        new_positions = head.move(direction, distance)
        
        tail_positions.extend(new_positions)
    
    print(len(set(tail_positions)))
    plt.plot([i[0] for i in tail_positions], [i[1] for i in tail_positions], '*')
    plt.grid(1)
    plt.show()
    
if __name__ == '__main__':
    run_sim('9dec/ex2.txt')