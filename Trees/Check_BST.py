import sys, threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

# Program to check if a Binary Tree is a BST
# Be careful about the input format.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBST(node, minimum, maximum):
    if(node is None):
        return True     # An empty Binary Tree is a BST (Base Case)

    if(node.data < minimum or node.data > maximum):
        return False    # Not a BST if Binary Tree violates BST property

    return (isBST(node.left, minimum, node.data - 1)) and (isBST(node.right, node.data + 1, maximum))


def main():
    n = int(input())
    if(n == 0):
        print("CORRECT")
        exit()

    temp = []
    nodes = []


    for i in range(n):
        key, left, right = map(int, input().split())
        temp.append([key, left, right])
        nodes.append(Node(key))

    for i in range(n):
        if(temp[i][1] != -1):
            nodes[i].left = nodes[temp[i][1]]
        if(temp[i][2] != -1):
            nodes[i].right = nodes[temp[i][2]]

    ans = isBST(nodes[0], float('-inf'), float('inf'))

    if(ans == True):
        print("CORRECT")

    else:
        print("INCORRECT")

threading.Thread(target=main).start()