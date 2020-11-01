import sys, threading
import queue

# Increasing Python recursion limit
sys.setrecursionlimit(10 ** 7)
threading.stack_size(2 ** 27)

# Class for a single node in the tree
class Node:
    def __init__(self, value):
        self.value = value
        self.children = [] # This array will store the children of any node in the tree as a Node object

    def AddChild(self, value):
        self.children.append(value)



class TreeHeight:
    def construct(self): # Taking input
        self.n = int(input())
        self.parent = list(map(int, input().split()))

    def Height(self):
        nodes = [Node(i) for i in range(self.n)] # Creating a list of all nodes
        for i in range(self.n):
            if(self.parent[i] == -1):
                self.root = nodes[i]

            else:
                nodes[self.parent[i]].AddChild(nodes[i])

        # BFS
        q = queue.Queue()
        q.put(self.root)
        height = 0

        while(not q.empty()):
            size = q.qsize()

            if(size > 0):
                height += 1
            
            for j in range(size):
                item = q.get()
                for i in item.children:
                    q.put(i)

        return height


def main():
    Tree = TreeHeight()
    Tree.construct()
    print(Tree.Height())
    

if __name__ == '__main__':
    main()


