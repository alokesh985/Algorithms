# This program will find the size of the largest group of 1s in a matrix
# of 0s and 1s (using DFS (manually))

def connectedCell(matrix):
    # Setting initial size as zero
    max_region_size = 0

    # Going through all elements in the matrix
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):

            if matrix[row][col] == 1:
                # If value is one, calculate size of neighbor region
                max_region_size = max(getRegionSize(matrix, row, col), max_region_size)

    return max_region_size

# Function to calculate neighbor size, using recursion (basically, DFS)
def getRegionSize(matrix, row, col):

    # If it goes out of bounds just return 0
    if(row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0])):
        return 0

    # If neighbor in 0, return 0 as the size of neighboring region will not increase 
    if(matrix[row][col] == 0):
        return 0

    # Setting matrix[row][col] to 0 as this will act like a visited check and
    # will prevent us checking the same value again and again
    matrix[row][col] = 0

    # Setting size as 1. We will return this as this will increase the size of the region by 1
    size = 1

    # Going from left and right neighbor of any element
    # From top and bottom of any element
    # Checking diagonal elements as well
    for row1 in range(row - 1, row + 2):
        for col1 in range(col - 1, col + 2):

            # Calling recursively to check other neighboring elements
            size += getRegionSize(matrix, row1, col1)

    # Returning size of the region
    return size

if __name__ == "__main__":

    rows = int(input("Enter Number of rows: "))
    cols = int(input("Enter Number of columns: "))

    matrix = [[0 for row in range(rows)] for col in range(cols)]

    ones = int(input("Enter number of 1s you want to have: "))

    for _ in range(ones):
        row, col = map(int, input("Enter row and column respectively: ").split())
        matrix[row][col] = 1

    print(f"Size of largest group of 1s: {connectedCell(matrix)}")