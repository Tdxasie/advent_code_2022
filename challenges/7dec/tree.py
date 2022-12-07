import treelib
from treelib import *
from collections import namedtuple
from uuid import uuid1
tree = Tree() # creating an object
tree.create_node("Harry", "harry")  # root node 
tree.create_node("Jane", "jane", parent="harry") #adding nodes
tree.create_node("Bill", "bill", parent="harry")
tree.create_node("Diane", "diane", parent="jane")
tree.create_node("Mary", "mary", parent="diane")
tree.create_node("Mark", "mark", parent="jane")
try:
    print(tree.create_node("Mark", "mark1", parent="diane"))
except treelib.exceptions.DuplicatedNodeIdError as e:
    print('love sos ')
tree.show()


File = namedtuple('File', 'size filename')


class Dir(treelib.Node):

    def __init__(self, name, id):
        super().__init__(name, id)
        self.files = []

    def add_file(self, size, filename):
        file = File(size, filename)
        if file not in self.files:
            self.files.append(File(size, filename))

id = uuid1()
tree.add_node(Dir('tgfrero', id), parent='mark1')
a = tree.get_node(id)
a.add_file('34', 'lovesos')
a.add_file('34', 'lovesos')
print(a.files)
tree.show()


a = tree.parent('diane').identifier
print(a)
