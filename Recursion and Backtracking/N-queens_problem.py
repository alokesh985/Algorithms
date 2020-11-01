# Function to print the board
def printBoard(board, n): 
	for i in range(n): 
		for j in range(n): 
			print(board[i][j], end = " ")
		print()


# Function to check if placing a queen is a safe move
def CheckSafety(board, row, col, n): 

	# Check left side 
	for i in range(col): 
		if board[row][i] == 1: 
			return False

	# Check upper left diagonal 
	for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
		if board[i][j] == 1: 
			return False

	# Check lower left diagonal 
	for i, j in zip(range(row, n, 1), range(col, -1, -1)): 
		if board[i][j] == 1: 
			return False

	return True

def NQueen(board, col, n): 
	# Base case 
	if col >= n: 
		return True

 
	for i in range(n): 

		if CheckSafety(board, i, col, n): 
			# Places a queen in [i][col] 
			board[i][col] = 1

			# Recursive call, backtracking 
			if NQueen(board, col + 1, n) == True: 
				return True

			board[i][col] = 0

	# If not possible, return False 
	return False

def main(): 

    n = int(input("Enter N, i.e., number of rows/columns: "))
    print()
    board = [[0 for col in range(n)] for row in range(n)]

    if NQueen(board, 0, n) == False: 
        print("SOLUTION DOES NOT EXIST!")
        return False


    print("1 indicates that a queen is present and 0 indicated that the spot in empty")
    printBoard(board, n) 
    return True

if __name__ == "__main__":
    main() 
