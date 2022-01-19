from typing import List

from Graph.Edge import Edge


class Path:
    __edges: List[Edge]

    def __init__(self):
        self.__edges = []

    def PrependEdge(self, edge: Edge):
        self.__edges.insert(0, edge)

    def __str__(self) -> str:
        if len(self.__edges) == 0:
            return "EMPTY PATH"

        path_str = ("(" + str(self.__edges[0].source) + ")")
        for edge in self.__edges:
            path_str += (" --" + str(edge.weight) + "--> (" + str(edge.destination) + ")")

        return path_str
