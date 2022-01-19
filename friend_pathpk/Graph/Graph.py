from typing import Dict, Any, Optional, Callable, List

from DataStructures.Queue import Queue
from Graph.Edge import Edge
from Graph.EdgeType import EdgeType
from Graph.Vertex import Vertex


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacencies = {}

    def __str__(self): # zamiana na string
        gStr = ''
        for vertex in self.adjacencies:
            gStr = gStr + 'Vertex(' + str(vertex) + ') -> neighbourhood: '
            for edge in self.adjacencies[vertex]: # destinatopn z edga, wszystkie krawedzie dla danego klucza
                gStr = gStr + 'Vertex(' + str(edge.destination) + '), '
            gStr = gStr + '\n'
        return gStr

    def create_vertex(self, data: Any) -> Vertex:
        i = len(self.adjacencies)
        v1 = Vertex(data, i)# index dlugosc slownika
        l1 = []
        self.adjacencies[v1] = l1# nowo stworzony vertex staje sie kluczem, przypisujemy pusta liste jako value
        return v1

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        e = Edge(source, destination, weight)
        if ((source in self.adjacencies.keys()) and (destination in self.adjacencies.keys())):# source i destination czy istnieja, laczenie
            self.adjacencies[source].append(e)#dodawanie pod kluczem source

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        e = Edge(source, destination, weight)# w dwie strony
        e2 = Edge(destination, source, weight)
        if ((source in self.adjacencies.keys()) and (destination in self.adjacencies.keys())):
            self.adjacencies[source].append(e)
            self.adjacencies[destination].append(e2) # tworzymy dwie krawedzie i dodajemy je do vertex

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:# dodawanie directed lub undirected
        if(edge == EdgeType.directed):
            self.add_directed_edge(source, destination, weight)
        if (edge == EdgeType.undirected):
            self.add_undirected_edge(source, destination, weight)

    # tylko dla grafow spojnych
    def traverse_breadth_first(self, visit: Callable[[Any], None]) -> None:
        vistedlist = []
        vertexqueue = Queue()

        vertexqueue.enqueue(next(iter(self.adjacencies))) # bierzemy pierwszy element i do listy i kolejki
        vistedlist.append(next(iter(self.adjacencies)))

        while(len(vertexqueue) != 0):
            v = vertexqueue.dequeue() # zdejmowanie z klejeki i visit
            visit(v)
            # wszystkie krawedzie polaczone z v, wyciaganie sasiadow
            for edge in self.adjacencies.get(v):
                neightbour = edge.destination
                if neightbour not in vistedlist: # jesli nie zostali odwiedzenie dodajemu do list i kolejki
                    vistedlist.append(neightbour)
                    vertexqueue.enqueue(neightbour)

    def traverse_depth_first(self, visit: Callable[[Any], None]) -> None:
        vistedlist = []
        tmpv = next(iter(self.adjacencies)) # 1 wierzcholek
        self.dfs(tmpv, vistedlist, visit) # rekurencja przez dfs




    def dfs(self, v: Vertex, visited: List[Vertex], visit: Callable[[Any], None]):
        # if (v in visited):
        #     return
        # else:
        #     visit(v)
        #     visited.append(v)
        visit(v)
        visited.append(v)
        for edge in self.adjacencies.get(v): # wszystkie krawedzie powiazane z v
            neightbour = edge.destination
            if (neightbour not in visited):# sprawdzanie sasiadow po wszystkich krawedziach czy nie sa w visited list
                self.dfs(neightbour, visited, visit)

    def show(self):
        for v in self.adjacencies: # po kluczach
            for edge in self.adjacencies[v]: # po wszystkich krawedziach dla danego klucza
                print( "([" + str(v) + "] --> [" + str(edge.destination) + "], " + str(edge.weight) + ")", end = ' ')
            if (len(self.adjacencies[v]) != 0):# dlugosc listy krawedzi dla danego klucza, usuwanie pustych linijek
                print('')
