def Mul_Naive(mat1, mat2):
    # O(n^3) Very slow
    p = len(mat1)
    q = len(mat1[0])

    m = len(mat2)
    n = len(mat2[0])

    if(q != m):
        print("Can't Multiply!")
        exit()

    ans = [[0 for col in range(n)] for row in range(q)]

    for row1 in range(len(mat1)):
        for col2 in range(len(mat2)):
            for row2 in range(len(mat2[0])):
                ans[row1][col2] += mat1[row1][row2] * mat2[row2][col2]

    return ans

if __name__ == "__main__":
    n = int(input("Enter Number of Matrices: "))

    matrices = []
    for i in range(n):
        row, col = map(int, input(f"Enter row and columns of matrix {i+1}: ").split())

        mat = []
        for r in range(row):
            temp = []
            for c in range(col):
                temp.append(int(input(f"Enter value {r+1},{c+1}: ")))

            mat.append(temp)

        matrices.append(mat)

    mat1, mat2 = map(int, input("Enter indices of matrices to multiply: ").split())

    ans = Mul_Naive(matrices[mat1], matrices[mat2])

    for row in range(len(ans)):
        for col in range(len(ans[0])):
            print(ans[row][col], end = " ")

        print()