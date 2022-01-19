from Graph.Graph import Graph
from Graph.EdgeType import EdgeType
from typing import *
# from DataStructures.Queue import Queue

if __name__ == '__main__':


    def friend_path(g: Graph, f0: Any, f1: Any) -> List[Any]:
        visited = []
        # q = Q
        queue = [[f0]]

        neighbours = []

        if f0 == f1:
            return []

        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in visited:
                for edge in g.adjacencies.get(node):
                    neighbours.append(edge.destination)

                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    queue.append(new_path)

                    if neighbour == f1:
                        print("shortest path = ", *new_path)
                        return new_path
                visited.append(node)

        print("Path doesnt' t exist")
        return []


    graph = Graph()

    vList = [
        graph.create_vertex("V0"),
        graph.create_vertex("V1"),
        graph.create_vertex("V2"),
        graph.create_vertex("V3"),
        graph.create_vertex("V4"),
        graph.create_vertex("V5")
    ]

    graph.add(EdgeType.undirected, vList[0], vList[1], 1)
    graph.add(EdgeType.undirected, vList[1], vList[2], 1)
    graph.add(EdgeType.undirected, vList[1], vList[5], 1)
    graph.add(EdgeType.undirected, vList[2], vList[3], 1)
    graph.add(EdgeType.undirected, vList[2], vList[4], 1)
    graph.add(EdgeType.undirected, vList[3], vList[4], 1)
    graph.add(EdgeType.undirected, vList[3], vList[5], 1)

    print(graph)
    print('\n')

    graph = Graph()

    vList = [
        graph.create_vertex("VI"),
        graph.create_vertex("RU"),
        graph.create_vertex("PA"),
        graph.create_vertex("CO"),
        graph.create_vertex("CH"),
        graph.create_vertex("RA"),
        graph.create_vertex("SU"),
        graph.create_vertex("KE")
    ]

    graph.add(EdgeType.undirected, vList[0], vList[4], 1)
    graph.add(EdgeType.undirected, vList[0], vList[1], 1)
    graph.add(EdgeType.undirected, vList[0], vList[2], 1)
    graph.add(EdgeType.undirected, vList[1], vList[5], 1)
    graph.add(EdgeType.undirected, vList[1], vList[6], 1)
    graph.add(EdgeType.undirected, vList[1], vList[0], 1)
    graph.add(EdgeType.undirected, vList[2], vList[3], 1)
    graph.add(EdgeType.undirected, vList[2], vList[7], 1)
    graph.add(EdgeType.undirected, vList[3], vList[1], 1)
    graph.add(EdgeType.undirected, vList[3], vList[0], 1)

    graph2 = Graph()
    vList2 = [
        graph2.create_vertex("jeden"),
        graph2.create_vertex("dwa"),
        graph2.create_vertex("trzy"),
        graph2.create_vertex("cztery"),
        graph2.create_vertex("piec"),
        graph2.create_vertex("szesc"),
        graph2.create_vertex("siedem"),
        graph2.create_vertex("osiem")
    ]

    graph2.add(EdgeType.undirected, vList2[0], vList2[4], 1)
    graph2.add(EdgeType.undirected, vList2[0], vList2[1], 1)
    graph2.add(EdgeType.undirected, vList2[0], vList2[2], 1)
    graph2.add(EdgeType.undirected, vList2[1], vList2[5], 1)
    graph2.add(EdgeType.undirected, vList2[1], vList2[6], 1)
    graph2.add(EdgeType.undirected, vList2[1], vList2[0], 1)
    graph2.add(EdgeType.undirected, vList2[2], vList2[3], 1)
    graph2.add(EdgeType.undirected, vList2[2], vList2[7], 1)
    graph2.add(EdgeType.undirected, vList2[3], vList2[1], 1)
    graph2.add(EdgeType.undirected, vList2[3], vList2[0], 1)

    graph3 = Graph()
    vList3 = [
        graph3.create_vertex("A"),
        graph3.create_vertex("B"),
        graph3.create_vertex("C"),


    ]
    graph3.add(EdgeType.undirected, vList3[0], vList3[2], 1)
    graph3.add(EdgeType.undirected, vList3[2], vList3[0], 1)
    graph3.add(EdgeType.undirected, vList3[0], vList3[1], 1)






    print(graph)
    print('\n')

    print(*friend_path(graph, vList[1], vList[7]))
    print('\n')


    print(graph2)
    print('\n')

    print(*friend_path(graph2, vList2[0], vList2[5]))

    print(graph3)
    print('\n')
    print(*friend_path(graph3, vList3[0], vList3[2]))