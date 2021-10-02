"""
    Attempt to create helper functions for a hash table.
    For more info: https://www.youtube.com/watch?v=ea8BRGxGmlA
"""


class HashTable:
    def __init__(self):
        self.max = 100
        self.array = [None for i in range(self.max)]

    def get_hash(self, key):
        """ Hash for a string. """
        hash_code = 0
        for char in key:
            hash_code += ord(char)
            return hash_code % 100

    def __getitem__(self, key, value):
        hash_code = self.get_hash(key)
        self.array[hash_code] = value

    def __setitem__(self, key, value):
        hash_code = self.get_hash(key)
        return self.array[hash_code]

    def __delitem__(self, key):
        hash_code = self.get_hash(key)
        self.array[hash_code] = None


# Usage Example
# m = HashTable()
# print(m.get_hash('random value'))
