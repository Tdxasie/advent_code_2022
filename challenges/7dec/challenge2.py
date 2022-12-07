from collections import namedtuple
import re
import treelib
from treelib import *
from uuid import uuid1


File = namedtuple('File', 'size filename')

class Dir(Node):
    def __init__(self, name, id, tree):
        super().__init__(name, id)
        self.files = []
        self._tree = tree

    def add_file(self, size, filename):
        file = File(size, filename)
        if file not in self.files:
            self.files.append(File(size, filename))

    def weight(self):
        files_weight = sum([f.size for f in self.files])
        dir_weights = sum([d.weight() for d in self._tree.children(self.identifier)])
        return files_weight + dir_weights

with open('input.txt') as infile:
    lines = infile.read().splitlines()


tree = Tree()
current_node = None
for line in lines:
    line = line.split(' ')
    if line[0] == '$':
        match line[1]:
            case 'cd':
                name = line[2]
                if name != '..':
                    try:
                        # add dir to tree and set to current
                        new_id = uuid1()
                        tree.add_node(Dir(name, new_id, tree), parent=current_node)
                        current_node = new_id
                    except treelib.exceptions.DuplicatedNodeIdError as e:
                        # find id of children existing dir
                        # set to current
                        children = tree.children(current_node)
                        for child in children:
                            if child.tag == name:
                                current_node = child.identifier
                                break
                elif name == '..':
                    current_node = tree.parent(current_node).identifier
                else:
                    print('cacaboudingz')
            case 'ls':
                continue
    elif line[0] == 'dir':
        continue
    elif re.match('\d+', line[0]):
        tree.get_node(current_node).add_file(int(line[0]), line[1])
    else:
        print('cacaboudingz')

tree.show()

total_space_availiable = 70_000_000
needed = 30_000_000


all_weights = sorted([d.weight() for d in tree.all_nodes()])
root_weight = all_weights[-1]


print(sorted([i for i in all_weights if i > needed-(total_space_availiable-root_weight)])[0])

tree.save2file('tree.txt')
