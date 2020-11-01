def Find_path(mat):
    routes = [[0 for cols in range(len(mat[0]))] for rows in range(len(mat))]

    routes[0][0] = mat[0][0]

    for i in range(1, len(mat[0])):
        routes[0][i] = (mat[0][i-1] + mat[0][i])

    for i in range(1, len(mat)):
        routes[i][0] = (mat[i-1][0] + mat[i][0])


    for i in range(1, len(mat)):
        for j in range(1, len(mat[0])):

            temp = min(routes[i-1][j], routes[i][j-1])

            routes[i][j] = (temp + mat[i][j])

    return routes[len(routes)-1][len(routes[0])-1]  

rows = int(input("Enter Number of rows: "))
cols = int(input("Enter Number of cols: "))

mat = [[0 for col in range(cols)] for row in range(rows)]

for i in range(rows):
    for j in range(cols):

        mat[i][j] = int(input(f"Enter Element Number [{i+1}][{j+1}]: "))


Min_Path = Find_path(mat)

print(f"Min Cost to go from 1st to last element in Matrix: {Min_Path}")