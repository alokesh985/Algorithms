# Prints connected components in adjacency matrix of graph

class Graph:

    def __init__(self, nodes):
        self.graph = [[0 for col in range(nodes)] for row in range(nodes)]
        self.vertices = []
        self.components = []

    def addEdge(self, fro, to):
        self.graph[fro][to] = 1
        self.graph[to][fro] = 1

        if fro not in self.vertices:
            self.vertices.append(fro)

        if to not in self.vertices:
            self.vertices.append(to)

    def connected_components(self):
        visited = {i : False for i in self.vertices}

        temp = []

        for node in self.vertices:
            if(visited[node] == False):

                self.DFSUtil(node, visited, temp)
                self.components.append(temp)
                temp = []

        return self.components

    def DFSUtil(self, node, visited, temp):
        temp.append(node)
        visited[node] = True

        for i in range(len(self.vertices)):

            if(self.graph[node][i] == 1 and visited[i] == False):
                self.DFSUtil(i, visited, temp)

    def printGraph(self):
        for fro in range(len(self.graph)):
            for to in range(len(self.graph)):

                if(self.graph[fro][to] == 1):
                    print(f"{fro} --> {to}")


n = int(input("Enter Number of nodes in graph: \n"))
g = Graph(n)

for i in range(n):

    fro, to = map(int, input("Enter fro and to respectively: ").split())

    g.addEdge(fro, to)

connected_components = g.connected_components()

print("Connected Components are: ")

for i in connected_components:
    print(*i)