class Graph:
    def __init__(self, vertices):
        self.graph = [[0 for cols in range(vertices)] for rows in range(vertices)]
        print(self.graph)

    def AddEdge(self, node, neighbour, weight):
        self.graph[node-1][neighbour-1] = weight
        self.graph[neighbour-1][node-1] = weight

    def PrintEdges(self):
        for i in range(len(self.graph)):
            for j in range(len(self.graph[0])):
                if(self.graph[i][j] != 0):
                    print(f"{i+1} --> {j+1}, Weight: {self.graph[i][j]}")

def main():
    num = int(input("Enter Number of vertices in the graph: "))
    
    graph = Graph(num)

    edges = int(input("Enter Number of edges in the graph: "))

    for i in range(edges):
        fro = int(input(f"Enter Source vertex for edge {i+1}: "))
        to = int(input(f"Enter Destination vertex for edge {i+1}: "))
        weight = int(input(f"Enter weight of edge {i+1}: "))

        graph.AddEdge(fro, to, weight)

    graph.PrintEdges()

if __name__ == "__main__":
    main()