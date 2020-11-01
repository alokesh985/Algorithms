class Graph:

    def __init__(self, V):
        self.graph = {}
        self.V = V

        self.nodes_list = []

    def AddEdge(self, fro, to):
        if(fro not in self.graph):
            self.graph[fro] = [to]
        else:
            self.grap[fro].append(to)

        if(fro not in self.nodes_list):
            self.nodes_list.append(fro)
        if(to not in self.nodes_list):
            self.nodes_list.append(to)

    def PrintEdges(self):
        for node in self.graph:
            for neighbour in self.graph[node]:
                print(f"{node} --> {neighbour}")

    def CyclicUtility(self, node, visisted, Rec_Stack):
        # Mark current node as visited and add to the recusrsion stack
        visisted[node] = True
        Rec_Stack[node] = True

        # For all neighbours on node, if any neighbour is in
        # recursion stack and visited at same time, cycle exists

        if(node in self.graph):
            for neighbours in self.graph[node]:
                if(visisted[neighbours] == False):
                    if(self.CyclicUtility(neighbours, visisted, Rec_Stack) == True):
                        return True

                elif(Rec_Stack[neighbours] == True):
                    return True

            # Remove element from recursion stack before returning if no cycle found
            Rec_Stack[node] = False
            return False

        else:
            return False

    def Cyclic(self):
        visited = {i : False for i in self.nodes_list}
        Rec_Stack = {i : False for i in self.nodes_list}

        # If a node is in visisted and rec_stack, then there is a cycle

        for node in self.nodes_list:
            if(visited[node] == False):
                if self.CyclicUtility(node, visited, Rec_Stack) == True:
                    return True
        return False


def main():
    nodes = int(input("Enter Number of nodes in graph: "))
    g = Graph(nodes)

    edges = int(input("Enter number of edges in the graph: "))
    for i in range(edges):

        fro, to = map(int, input("Enter source and destination node: ").split())

        g.AddEdge(fro, to)

    if(g.Cyclic() == True):
        print("Graph Is Cyclic")
    else:
        print("Graph has no cycles")

if __name__ == "__main__":
    main()