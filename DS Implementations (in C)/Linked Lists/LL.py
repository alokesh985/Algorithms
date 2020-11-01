# Python3 implementation of LinkedList

class Node:
    def __init__(self, value = 0, next = None): # Default value of a node is 0
        self.data = value
        self.next = next

    def Print(self, head):
        ptr = head

        while(ptr != None):
            print(f"{ptr.data} --> ", end = "")
            ptr = ptr.next

        print()

def main():
    head_value = int(input("Enter head value: "))
    head = Node(head_value)

    while(True):
        choice = int(input("Enter 1 to Enter new node, 2 to print and 3 for exit: "))
        if(choice == 1):
            temp = int(input("Enter Node Value: "))
            ptr = head
            while(ptr.next != None):
                ptr = ptr.next

            new_node = Node(temp)

            ptr.next = new_node

        elif(choice == 2):
            head.Print(head)

        else:
            break

            


if __name__ == "__main__":
    main()