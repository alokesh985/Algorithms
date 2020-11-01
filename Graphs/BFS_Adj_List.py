from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.node_list = []

    def AddEdge(self, fro, to):
        self.graph[fro].append(to)

        if(fro not in self.node_list):
            self.node_list.append(fro)
        if(to not in self.node_list):
            self.node_list.append(to)

    def BFS(self, start):
        visited = {i : False for i in self.node_list}
        traversal = []

        q = []

        q.append(start)
        visited[start] = True

        while(len(q) > 0):
            popped = q.pop(0)
            traversal.append(popped)

            for neighbour in self.graph[popped]:
                if(visited[neighbour] == False):
                    q.append(neighbour)
                    visited[neighbour] = True

        
        return traversal

def main():
    g = Graph()

    edges = int(input("Enter Number of Edges in the graph: "))

    for i in range(edges):
        fro = int(input(f"Enter Source Vertex for Edge {i+1}: "))
        to = int(input(f"Enter Destination Vertex for Edge {i+1}: "))

        g.AddEdge(fro, to)

    start = int(input("Enter Vertex to begin BFS with: "))
    traversal = g.BFS(start)

    print(*traversal)

if __name__ == "__main__":
    main()

