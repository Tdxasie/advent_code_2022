import re

pattern = r"Monkey\s(?P<id>\d):\n.+:(?P<items>(?:\s\d+(\n|,))+).+d\s(?P<op>.)\s(?P<val>\d+|\w+)\n.+y\s(?P<div>\d+)\n.+y\s(?P<true>\d)\n.+y\s(?P<false>\d+)"

regexp = re.compile(pattern)

operations = {
    '+': lambda a, b: a+b,
    '*': lambda a, b: a*b
}

ROUNDS = 10_000


class Monkey:
    def __init__(self, id):
        self.id = id
        self.items = None
        self.op = None
        self.div = None
        self.dest_true = None
        self.dest_false = None
        self.inspections = 0

    def set_items(self, items):
        items = items.strip().split(', ')
        self.items = [int(i) for i in items]

    def set_op(self, op, val):
        op = operations[op]
        if val == 'old':
            self.op = lambda x: x
        else:
            self.op = lambda x: op(x, int(val))

    def throw_items(self, monkeys):
        for item in self.items:
            # monkey inspects item
            item = self.op(item)
            self.inspections += 1
            # worry levels skyrocket
            # item = int(item/3)
            dest = [self.dest_false, self.dest_true][item % self.div == 0]
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
        # for monkey in monkeys:
        #     print(f'Monkey {monkey.id} : {monkey.items}')

    inspections = [m.inspections for m in monkeys]
    a = sorted(inspections)[-2:]
    print(a[0]*a[1])


if __name__ == '__main__':
    run_chal1('11dec/ex.txt')
