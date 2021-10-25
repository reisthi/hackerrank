class Node(object):
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


class LinkedList(object):
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def get_size(self):
        return self.size

    def add_node(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def find(self, data):
        current_node = self.root
        while current_node:
            if current_node.get_data() == data:
                return data
            else:
                current_node = current_node.get_next()
        return None

    def remove(self, data):
        current_node = self.root  # start at root node
        prev_node = None
        while current_node:
            if current_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(current_node.get_next())
                else:
                    self.root = current_node
                self.size -= 1
                return True  # data removed
            else:
                prev_node = current_node
                current_node = current_node.get_next()
        return False


