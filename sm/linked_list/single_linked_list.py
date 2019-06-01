import sys
sys.path.append('..')
from sm.linked_list.node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._node = Node
        self.d_size = 0

    def empty(self):
        if self.d_size == 0:
            return True
        else:
            return False

    def size(self):
        return self.d_size

    def append(self, data):
        new_node = self._node(data)

        if self.empty():
            self.head = new_node
            self.tail = new_node
            self.d_size += 1

        else:
            self.tail.next = new_node
            self.tail = new_node
            self.d_size += 1

    def search_target(self, target, start=0):
        if self.empty():
            return None
        pos = 0
        cur = self.head

        if pos >= start and target == cur.data:
            return cur.data, pos

        while cur.next:
            pos += 1
            if pos >= start and target == cur.data:
                return cur.data, pos
        return None, None

    def delete(self, data):
        if self.empty():
            return None
        data

def show_list(slist):
    if slist.empty():
        print('The list is empty')
        return

    for i in range(slist.size()):
        print(slist.search_target(i), end=' ')

if __name__ == '__main__':
    slist = LinkedList()
    print('데이터 개수: {}'.format(slist.size()))
    show_list(slist)
    print()
    slist.append(3)
    slist.append(1)
    slist.append(2)
    slist.append(5)

    print('데이터 개수: {}'.format(slist.size()))
    show_list(slist)
    print()
