from collections import deque


class Cache:
    def __init__(self):
        self.values = deque(maxlen=3)


    def soma(self, *args):
        result = 0
        self.values.append(args)
        for arg in args:
            result += arg
        return result


    def __repr__(self):
        return f"{(', ').join(str(x) for x in self.values )}"