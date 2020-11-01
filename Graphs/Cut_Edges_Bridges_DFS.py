# Undirected graph

class Graph:

    def __init__(self):
        self.graph = {}
        self.time = 0

    def AddEdge(self, fro, to):
        if(fro not in self.graph):
            self.graph[fro] = [to]
        else:
            self.graph[fro].append(to)

        if(to not in self.graph):
            self.graph[to] = [fro]
        else:
            self.graph[to].append(fro)


    def PrintGraph(self):

        for i in self.graph:
            for j in self.graph[i]:
                print(f"{i} --> {j}")

    def CutEdges(self):

        # List to keep track of visited vertices
        
        visited = {i : False for i in self.graph}

        # List to store cut edges
        cut_edges = []

        # To keep track of discovery time of vertices
        discovery = {i : float("inf") for i in self.graph}

        # low[u] = min(discpvery[u], discovery[w]) 
        # where w is an ancestor of u and there is a back edge from 
        # some descendant of u to w.

        low = {i : float("inf") for i in self.graph}

        # parent[u] stores parent of u
        parent = {i : -1 for i in self.graph}
        
        for node in self.graph:

            if(visited[node] == False):
                self.Util(node, visited, parent, low, discovery, cut_edges)

        return cut_edges

    def Util(self, node, visited, parent, low, discovery, cut_edges):
        visited[node] = True

        discovery[node] = self.time
        low[node] = self.time
        self.time += 1

        for neighbour in self.graph[node]:

            if(visited[neighbour] == False):
                parent[neighbour] = node

                self.Util(neighbour, visited, parent, low, discovery, cut_edges)

                # Check if subtree of neighbour has any connection with ancestor of node
                low[node] = min(low[node], low[neighbour])

                if(low[neighbour] > discovery[node]):
                    cut_edges.append((node, neighbour))

            elif(neighbour != parent[node]):
                low[node] = min(low[node], discovery[neighbour])


g = Graph()
edges = int(input("Enter number of edges in the graph: "))

for _ in range(edges):
    fro, to = map(int, input("Enter source and destination respectively: ").split())

    g.AddEdge(fro, to)

cut_edges = g.CutEdges()

print("Cut Edges Are: ")
for edge in cut_edges:
    print(f"{edge[0]} ----> {edge[1]}")