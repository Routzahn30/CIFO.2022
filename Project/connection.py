import random

vehicle_list = []


class Connection(object):

    def __init__(self):
        self.path = sorted(vehicle_list, key=lambda *args: random.random())
        self.connection_length

    def connection_length(self):
        self.length = 0
        for point in self.path:
            next_point = self.path[self.path.index(point)-len(self.path)+1]

