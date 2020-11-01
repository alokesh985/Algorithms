# Connected components in an undirected graph using DFS
# Uses adjacency list
class Graph:
    def __init__(self):
        self.graph = {}
        self.vertices = []
        self.components = []

    def addEdge(self, fro, to):
        if(fro not in self.graph):
            self.graph[fro] = [to]
        else:
            self.graph[fro].append(to)

        if(to not in self.graph):
            self.graph[to] = [fro]
        else:
            self.graph[to].append(fro)

        if fro not in self.vertices:
            self.vertices.append(fro)

        if to not in self.vertices:
            self.vertices.append(to)

    def connectedComponents(self):
        visited = {i : False for i in self.vertices}
        count = 0

        temp = []
        
        for node in self.vertices:
            if(visited[node] == False):

                self.DFSUtil(node, visited, temp)
                count += 1
                self.components.append(temp)
                temp = []

        return self.components

    def DFSUtil(self, node, visited, temp):
        visited[node] = True  
        temp.append(node)      
        
        for neighbour in self.graph[node]:

            if(visited[neighbour] == False):

                self.DFSUtil(neighbour, visited, temp)

        


    

g = Graph()
nodes = int(input("Enter number of nodes in list: "))
for i in range(nodes):
    fro, to = map(int, input("Enter fro and to respectively: ").split())
    g.addEdge(fro, to)

components = g.connectedComponents()

print("The connected components are: ")

for component in components:
    print(*component)