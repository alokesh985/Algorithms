# Undirected graph

class Graph:
    def __init__(self):
        self.graph = {}
        self.time = 0

    def addEdge(self, fro, to):
        if(fro not in self.graph):
            self.graph[fro] = [to]
        else:
            self.graph[fro].append(to)

        if(to not in self.graph):
            self.graph[to] = [fro]
        else:
            self.graph[to].append(fro)

    def PrintEdges(self):
        for node in self.graph:
            for neighbour in self.graph[i]:
                print(f"{node} --> {neighbour}")

    def CutVerticesUtil(self, node, visited, cv_list, parent, low, discovery):
        # Count of number of children of node
        children = 0

        visited[node] = True

        # This is when the node is discovered
        discovery[node] = self.time
        low[node] = self.time
        self.time += 1

        # Recur for all neighours of node

        for neighbour in self.graph[node]:

            if(visited[neighbour] == False):

                # node's children increase
                parent[neighbour] = node
                children += 1
                self.CutVerticesUtil(neighbour, visited, cv_list, parent, low, discovery)

                ''' Check if the subtree rooted at neighbour has any connection with ancestor
                    of node'''

                low[node] = min(low[node], low[neighbour])

                # node is a cut vertex / articulation point in the following 2 cases

                # Case 1: node is root and has >=2 children
                if(parent[node] == -1 and children >= 2):
                    cv_list[node] = True

                # Case 2: If node is not root, check if any of it's children is discovered
                # before node (i.e., if low value of any of it's children is more than it's
                # discovery value)
                if(parent[node] != -1 and low[neighbour] >= discovery[node]):
                    cv_list[node] = True

            
            elif(neighbour != parent[node]):
                low[node] = min(low[node], discovery[neighbour])

    def CutVertices(self):
        cut_vertices = []

        visited = {i : False for i in self.graph}
        # Stores discovery time of vertices, i.e., ancestors
        discovery = {i : float("Inf") for i in self.graph}

        ''' low[u] = min(discpvery[u], discovery[w]) 
            where w is an ancestor of u and there is a back edge from 
            some descendant of u to w. '''

        low = {i : float("Inf") for i in self.graph}

        # parent[u] stores parent of vertex u
        parent = {i : -1 for i in self.graph}

        # True means it is a cut vertex
        cv_list = {i : False for i in self.graph}

        for node in self.graph:
            if(visited[node] == False):
                self.CutVerticesUtil(node, visited, cv_list, parent, low, discovery)

        for node in cv_list:
            if(cv_list[node] == True):
                cut_vertices.append(node)

        return cut_vertices


def main():
    graph = Graph()

    edges = int(input("Enter Number of edges in the graph: "))

    for i in range(edges):
        fro, to = map(int, input("Enter source and destination: ").split())

        graph.addEdge(fro, to)

    cut_vertices = graph.CutVertices()

    print("Cut Vertices: ",end = "")

    print(*cut_vertices)

if __name__ == "__main__":
    main()