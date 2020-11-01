# Full Pyramid

n = int(input())

tot = (2 * n) - 1

spaces = tot // 2
stars = 1

for i in range(n):
    for j in range(spaces):
        print(" ",end = "")

    for j in range(stars):
        print("*", end = "")

    for j in range(spaces):
        print(" ", end="")

    stars += 2
    spaces -= 1
    print()


