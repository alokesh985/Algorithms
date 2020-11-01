n = int(input())

tot = (2 * n) - 1

star = tot // 2
dec = 1
for i in range(n):
    if(i == 0):
        for j in range(tot):
            if(j == star):
                print("*", end = " ")
            else:
                print(" ", end = " ")

    elif(i == n-1):
        for j in range(tot):
            print("*", end = " ")

    else:
        front = star - dec
        back = star + dec
        dec += 1

        for i in range(tot):
            if(i == front or i == back):
                print("*", end = " ")
            else:
                print(" ", end = " ")

    print()
