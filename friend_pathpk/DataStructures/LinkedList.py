from typing import Any

from DataStructures import Node


class LinkedList:
    head: Node
    tail: Node

    def __init__(self, node: Node = None):
        self.head = node
        self.tail = node

    def __len__(self):
        node = self.head
        n: int = 0
        while node != None:
            n += 1
            node = node.next
        return n

    def __str__(self):
        st = ""
        node = self.head
        for x in range(len(self)):
            if node.next != None:
                st += str(node.value) + " -> "
            if node.next == None:
                st += str(node.value)
            node = node.next
        return st

    def push(self, value: Any)->None :
        node = Node(value)
        if (self.head == None):
            self.head = node
            self.tail = node
        else:
            tmp = self.head
            self.head = node
            node.next = tmp # sklejanie

    def append(self, value: Any)->None:
        node = Node(value)
        if (self.tail == None):
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    def node(self, at: int)-> Node:
        tmp= self.head
        while (at >0):
            at= at -1 # warunek iterujacy od konca noda
            if (tmp == None):
                break
            else:
                tmp = tmp.next
        return tmp
    def insert(self, value: Any, after: Node):
        node = Node(value)
        tmp = self.head
        while(tmp != after):
            tmp = tmp.next
            if (tmp.next == None):
                raise ValueError("Node value out of list")
        node.next = tmp.next # nowo stworzony node wskazuje na next node
        tmp.next = node

    def pop(self)->Any:
        if (self.head == None):
            return None
        tmp = self.head
        self.head = tmp.next
        return tmp

    def remove_last(self) -> Any:

        if (self.tail == None):
            raise ValueError("Empty queue")

        elif (self.head == self.tail):
            tmp = self.head
            self.head = None
            self.tail = None
            return tmp
        else:
            tmp = self.tail
            self.tail = self.node(self.len() - 2)  # ogon naszej list = przedostatni element
            self.node(self.len() - 2).next = None  # mowimy ze ostatni element jest usuniety
            return tmp

    def len(self)->int:
        tmp = self.head
        n:int = 0
        while (tmp != None):
            tmp = tmp.next
            n = n + 1
        return n

    def remove(self, after: Node)->Any:
        tmp = self.head
        while (tmp != after):
            if (tmp == None):
                return
            tmp = tmp.next
        if (tmp.next == None):
            return
        else:
            tmp.next = tmp.next.next

    # def print(self)->None:
    #     node = self.head
    #     while(node != None):
    #         print(node.value)
    #         node = node.next # iteracja

