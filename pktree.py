from typing import Any, List

class TreeNode:
    value : Any
    children : List['TreeNode']

    def __init__(self, value : Any, children : List):
        self.value = value
        self.children = []

    def is_leaf(self)-> bool:
        if(self.children == None):
            return True
        return False

    def add(self, child: 'TreeNode')-> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: callable[['TreeNode'], None])-> None:
        if (visit != None):
            return
        visit(self)
        for child in self.children:
            if (not child.visit):
                return
            for child in self.children:
                self.for_each_deep_first(visit(child))

    def for_each_level_order(self, visit: callable[['TreeNode'], None])-> None:
        if (visit != None):
            return
        fifo = self.children
        if( fifo != None):
            for i in len(fifo):
                print(fifo[0])
                fifo += fifo[0]



















class Tree:
    root : TreeNode


    def __init__(self, root):
        self.root = root
    def add(self, value: Any, parent_name : Any)->None:
        TreeNode.add(value, parent_name)

kids : TreeNode = TreeNode()

kids.add("os")












