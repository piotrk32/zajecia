from typing import Any, List

class TreeNode:
    value: Any
    children: List['TreeNode']


    def __init__(self,value: Any,children: List):
        self.value=value
        self.children=children
    def is_leaf(self)-> bool:
        if(self.children==None):
            return True
        else:
            return False
    def add(self,child: 'TreeNode') -> None:
        self.children.append(child)
    def __str__(self) -> str:
        wynik = self.value
        return wynik





class Tree:
    root: TreeNode

    def __init__(self,root):
        self.root=root

    def add(self,value: Any,parent_name:Any) -> None:
        TreeNode.add(value,parent_name)




dzieci: TreeNode= TreeNode()