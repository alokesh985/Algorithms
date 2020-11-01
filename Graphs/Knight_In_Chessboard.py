""" This program will find the shortest path that a knight in a given N*N chessboard will take to go
to a target cell on the chessboard.
This uses BFS, as we are basically finding the shortest path in an unweighted graph
 """

# Represents one cell of the chessboard
class cell:

    # distance gives the distance from the initial position 
    def __init__(self, x = 0, y = 0, distance = 0):
        self.x = x
        self.y = y
        # distance is basically the number of moves to get to the target cell on the chessboard
        self.distance = distance

# Function to check if the cell is valid i.e., check if the cell lies inside the chessboard
def isValid(x, y, N):
    if(x >= 1 and x <= N and y >= 1 and y <= N):
        return True
    else:
        return False

# Actual function that will do the work
def minPath(current_position, target_position, N):

    # All the valid moves a knight can make (This is according to actual chess moves)
    valid_x = [2, 2, -2, -2, 1, 1, -1, -1]
    valid_y = [1, -1, 1, -1, 2, -2, 2, -2]

    # Queue for BFS
    queue = []

    # Starting at (0, 1)
    queue.append(cell(current_position[0], current_position[1], 0))

    # Create a 'visited' 2D matrix to keep track of which cells are visited
    visited = [[False for i in range(N + 1)] for j in range(N + 1)]

    # Visit the (0, 1) position (initial position)
    visited[current_position[0]][current_position[1]] = True

    # Loop till queue is not empty
    while(len(queue) > 0):

        temp = queue.pop(0)

        if(temp.x == target_position[0] and temp.y == target_position[1]):
            return temp.distance

        # We are taking 8  because there are 8 possible moves and we have to check each one of them
        for i in range(8):

            x = temp.x + valid_x[i]
            y = temp.y + valid_y[i]

            if(isValid(x, y, N) and visited[x][y] == False):
                visited[x][y] = True
                queue.append(cell(x, y, temp.distance + 1))

def main():
    N = int(input("Enter value of N in an N*N chessboard: "))

    initial_position = list(map(int, input("Enter initial position of knight in x and y: ").split()))
    target_position = list(map(int, input("Enter target postion of knight in x and y: ").split()))

    print(f"Minimum number of moves needed: {minPath(initial_position, target_position, N)}")

if __name__ == "__main__":
    main()