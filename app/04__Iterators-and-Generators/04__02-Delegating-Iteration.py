# PROBLEM:  Would like to make iteration with new custom container that holds a list, tuple, 
#           or another iterable
# SOLUTION: Deine __iter__() method to delegate iteration of internal container

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        # must implement a next()
        return iter(self._children)

# Example
if __name__ == '__main__':
    root = Node(0)
    print('Root: %s ' % root)
    child1 = Node(1)
    print('child1: %s ' % child1)
    child2 = Node(2)
    print('child2: %s ' % child2)
    root.add_child(child1)
    print('Root + child1: %s ' % root)
    root.add_child(child2)
    print('Root + child2: %s ' % root)

    for ch in root:
        print(ch)