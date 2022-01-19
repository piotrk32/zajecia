from typing import Any


class Node:
    value: Any
    next: 'Node'

    def __init__(self, value):
        self.value = value
        self.next = None
