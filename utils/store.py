class Store():
    def __init__(self):
        self.map = dict()

    def add_item(self, key, value):
        self.map[key] = value

    def read_item(self, key):
        return self.map[key]

    def remove_item(self, key):
        self.map.pop(key)

    def exist_item(self, key):
        return key in self.map