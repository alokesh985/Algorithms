""" Note that 0 is a falsy value in Python. So if a node's data is 0, it will evaluate to False here. 
Make sure to check code for this. """

class Tree:
    def __init__(self, data):
        # Setting this for root value
        self.data = data
        self.left = None
        self.right = None

    def Insert(self, data):
        if(self.data): # Checking if root is present

            if(data <= self.data): # If value of new node is less than or equal to root
                if(self.left == None):# If not value on left of root new node's value is less than root.
                    self.left = Tree(data) # Creating a new node (subtree)
                else:
                    self.left.Insert(data) # Recursively add new node to left subtree

            elif(data > self.data):
                if(self.right == None):# If not value on right of root new node's value is less than root.
                    self.right = Tree(data) # Creating a new node (subtree)
                else:
                    self.right.Insert(data) # Recursively add new node to right subtree

        else: # If root does not exist
            self.data = data

    def Inorder_Traversal(self):
        if(self.data): # If root exists
            
            if(self.left):
                self.left.Inorder_Traversal()
            
            print(self.data, end = " ")

            if(self.right):
                self.right.Inorder_Traversal()



    def PreOrder_Traversal(self):
        if(self.data):
            
            print(self.data, end = " ")

            if(self.left):
                self.left.PreOrder_Traversal()

            if(self.right):
                self.right.PreOrder_Traversal()

    def PostOrder_Traversal(self):
        if(self.data):
            
            if(self.left):
                self.left.PostOrder_Traversal()

            if(self.right):
                self.right.PostOrder_Traversal()

            print(self.data, end = " ")


def main():
    nodes = int(input("Enter Number of Nodes In the Tree: "))
    root = int(input("Enter root Element value: "))

    tree = Tree(root)

    for i in range(nodes - 1): # (nodes - 1) because we have already inserted root

            ip = int(input(f"Enter node {i+1} value: "))
            tree.Insert(ip)

    print("The Inorder Traversal Is: ", end = "")
    tree.Inorder_Traversal()
    print()

    print("The PreOrder Traversal Is: ", end = "")
    tree.PreOrder_Traversal()
    print()

    print("The PostOrder Traversal Is: ", end = "")
    tree.PostOrder_Traversal()
    print()

if __name__ == "__main__":
    main()