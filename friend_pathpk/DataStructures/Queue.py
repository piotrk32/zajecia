from typing import Any

from DataStructures.LinkedList import LinkedList


class Queue:

    def __init__(self):
        self._storage = LinkedList()

    def __len__(self):
        return len(self._storage)

    def __str__(self):
        st = ""
        N = len(self._storage)
        for i in range(len(self._storage)):
            st += str(self._storage.node(N - i -1).value) + " "
        return st

    def peek(self)->Any:
        if len(self._storage) != 0:
            return self._storage.tail.value
        else:
            raise ValueError("Queue is empty")

    def enqueue(self, element: Any) -> None:
        self._storage.push(element)

    def dequeue(self)->Any:
        while (len(self._storage) != 0):
            return self._storage.remove_last().value
        else:
            raise ValueError("Queue is empty")

    def pop(self) -> Any:
        if (self.head == None):
            return None
        tmp = self.head
        self.head = tmp.next
        return tmp
