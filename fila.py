from collections import deque

class Fila:
    def __init__(self):
        self.fila = deque()

    def insere(self, val):
        self.fila.append(val)

    def remove(self):
        return self.fila.popleft()

    def __repr__(self):
        return f"Fila [{', '.join(str(x) for x in self.fila)}]"
