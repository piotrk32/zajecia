from typing import Any

from LinkedList import LinkedList


class Stack:



    def __init__(self):
        self._storage = LinkedList()

    def __len__(self):
        return len(self._storage)

    def __str__(self):
        st = ""
        for i in range(len(self._storage)):
            st += "+" + str(self._storage.node(i).value) + "+\n"
        return st

    def push(self, value)-> None:
        self._storage.push(value)

    def pop(self)-> Any:
        return self._storage.pop().value