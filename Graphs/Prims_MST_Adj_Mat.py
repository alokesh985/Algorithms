# Using adjacency matrix, bidirectional

class Graph:

    def __init__(self, v):
        self.graph = [ [0 for i in range(v)] for j in range(v) ]
        self.vertices = v
        self.edges = 0

    def AddEdge(self, fro, to, weight):
        self.graph[fro][to] = weight
        self.graph[to][fro] = weight
        self.edges += 1


    def Prims(self):
        if(self.edges < (self.vertices - 1)):
            print("Graph is not connected. No MST")
            exit()

        # Array to keep track of vertices that are visited
        visited = [False] * self.vertices

        # No. of edges in MST
        MST_Edges = 0

        # The number of edges in an MST will always be equal to n-1, where
        # n is the no. of nodes in the graph

        # Starting for first vertex
        visited[0] = True

        total_weight = 0
        while(MST_Edges != (self.vertices - 1)):
            # For every vertex, find all its adjacent vertices and calculate weight
			# . Pick the one with minimum weight. If vertex is not visited yet, 
			# add it to the MST.

            min = float("inf")
            x, y = 0, 0

            for i in range(self.vertices):
                if(visited[i] == True):

                    for j in range(self.vertices):
                        if(visited[j] == False and self.graph[i][j] != 0):
                            # If not visited yet, an edge exists

                            if(self.graph[i][j] < min):
                                min = self.graph[i][j]

                                x, y = i, j
            total_weight += self.graph[x][y]
            print(f"{x} --> {y}, weight: {self.graph[x][y]}")

            visited[y] = True
            MST_Edges += 1
        print(f"Total Cost: {total_weight}")
                

    def PrintGraph(self):
        for i in range(len(self.graph)):
            for j in range(len(self.graph[0])):
                print(self.graph[i][j], end = " ")

            print()

nodes = int(input("Enter Number of nodes in graph: "))

graph = Graph(nodes)

edges = int(input("Enter Number of Edges: "))

for i in range(edges):
    fro, to, weight = map(int, input("Enter source, destination and weight respectively: ").split(" "))
    graph.AddEdge(fro, to, weight)

graph.Prims()