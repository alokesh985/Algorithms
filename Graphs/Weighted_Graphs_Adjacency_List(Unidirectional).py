class Graph:
    def __init__(self):
        self.graph = {}

    # The graph will be stored as Node: [(Neighbour, Weight), ...]
    def addEdge(self, node, neighbour, weight):
        if node not in self.graph:
            self.graph[node] = []
            self.graph[node].append((neighbour, weight))

        else:
            self.graph[node].append((neighbour, weight))

    def PrintEdges(self):

        for nodes in self.graph:
            for neighbours in self.graph[nodes]:

                print(f"{nodes} --> {neighbours[0]}, Weight: {neighbours[1]}")


def main():
    graph = Graph()

    edges = int(input("Enter Number of edges in the graph: "))

    for i in range(edges):
        fro = int(input("Enter Source Node: "))
        to = int(input("Enter Destination Node: "))
        weight = int(input("Enter Weight of the Edge: "))

        graph.addEdge(fro, to, weight)

    graph.PrintEdges()

if __name__ == "__main__":
    main()