class Node(object):
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.previous_node = prev_node
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next_node()

    def set_next(self, next_node):
        self.next_node = next_node

    def get_previous(self):
        return self.previous_node()

    def set_previous(self, prev_node):
        self.previous_node = prev_node


class DoublyLinkedList(object):

    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def get_size(self):
        return self.size

    def add(self, data):
        new_node = Node(data, self.root)
        if self.root:
            self.root.set_previous(new_node)
        self.root = new_node
        self.size += 1

    def remove(self, data):
        current_node = self.root
        while current_node:
            if current_node.get_data == data:
                next_node = current_node.get_next()
                prev_node = current_node.get_previous()

                if next_node:
                    next_node.set_previous(prev_node)
                if prev_node:
                    prev_node.set_next(next_node)
                else:
                    self.root = current_node

