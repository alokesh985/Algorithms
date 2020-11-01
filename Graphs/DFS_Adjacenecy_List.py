class Graph:
    def __init__(self):
        self.graph = {}
        self.traversal = []

    def AddEdge(self, fro, to):
        if(fro not in self.graph):
            self.graph[fro] = [to]
        else:
            self.graph[fro].append(to)

        if(to not in self.graph):
            self.graph[to] = [fro]
        else:
            self.graph[to].append(fro)

    def DFSUtil(self, start, visited):
        visited[start] = True
        self.traversal.append(start)

        for node in self.graph[start]:
            if(visited[node] == False):
                self.DFSUtil(node, visited)

    def DFS(self, start):
        visited = [False] * (max(self.graph) + 1)
        self.DFSUtil(start, visited)
        
    def Print(self):
        print(*self.traversal)


g = Graph()

g.AddEdge(0, 3) 
g.AddEdge(0, 1)
g.AddEdge(0, 2)
g.AddEdge(2, 1)
g.AddEdge(2, 4)


g.DFS(2)

g.Print()
    