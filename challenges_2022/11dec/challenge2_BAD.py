import re
from uuid import uuid1

pattern = r"Monkey\s(?P<id>\d):\n.+:(?P<items>(?:\s\d+(\n|,))+).+d\s(?P<op>.)\s(?P<val>\d+|\w+)\n.+y\s(?P<div>\d+)\n.+y\s(?P<true>\d)\n.+y\s(?P<false>\d+)"

regexp = re.compile(pattern)

operations = {
    '+': lambda a, b: a+b,
    '*': lambda a, b: a*b
}

ROUNDS = 10_000


class Item:
    def __init__(self, initial_worry):
        self.id = uuid1()
        self.initial_worry = initial_worry
        self.worry = initial_worry

    def reset_worry(self):
        self.worry = self.initial_worry
class Monkey:
    def __init__(self, id):
        self.id = id
        self.items = None
        self.op = None
        self.div = None
        self.dest_true = None
        self.dest_false = None
        self.inspections = 0
        self.item_ops = {}

    def set_items(self, items):
        items = items.strip().split(', ')
        self.items = [Item(int(i)) for i in items]

    def set_op(self, op, val):
        op = operations[op]
        if val == 'old':
            self.op = lambda x: op(x, x)
        else:
            self.op = lambda x: op(x, int(val))

    def throw_items(self, monkeys):
        for item in self.items:
            # monkey inspects item
            item.worry = self.op(item.worry)
            self.inspections += 1
            # worry levels skyrocket

            if item.id not in self.item_ops.keys():
                self.item_ops[item.id] = []
                
            dest = [self.dest_false, self.dest_true][item.worry % self.div == 0]
            if dest in self.item_ops[item.id]:
                item.reset_worry()
                self.item_ops[item.id] = []
            else:
                self.item_ops[item.id].append(dest)
            monkeys[dest].items.append(item)
        self.items = []


def run_chal1(filename):
    with open(filename) as infile:
        lines = infile.read()

    instructions = [m.groupdict() for m in regexp.finditer(lines)]

    # make monkeys
    monkeys = []
    for inst in instructions:
        m = Monkey(int(inst['id']))
        m.set_items(inst['items'])
        m.set_op(inst['op'], inst['val'])
        m.div = int(inst['div'])
        m.dest_true = int(inst['true'])
        m.dest_false = int(inst['false'])
        monkeys.append(m)

    for i in range(ROUNDS):
        print(f'Round {i}')
        for monkey in monkeys:
            monkey.throw_items(monkeys)

    inspections = [m.inspections for m in monkeys]
    a = sorted(inspections)[-2:]
    print(a[0]*a[1])


if __name__ == '__main__':
    run_chal1('11dec/input.txt')
