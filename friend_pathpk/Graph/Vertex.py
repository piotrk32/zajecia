from typing import Any


class Vertex:
    data: Any
    index: int

    def __init__(self, data, index):
        self.data = data
        self.index = index

    def __str__(self):
        return str(self.index) + " " + str(self.data)

    def __hash__(self): # vertex z klasy Vertex zrobienie klucza na mapie ??
        return hash((self.data, self.index))

    def __eq__(self, other):# porownywanie vertexow, napidsanie == miedzy vertexami
        return (self.data, self.index) == (other.data, other.index)