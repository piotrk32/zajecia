from typing import Optional

from Graph.Vertex import Vertex


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __str__(self):
        return str(self.source) + " " + str(self.destination) + " " + str(self.weight)
