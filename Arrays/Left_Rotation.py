# Number left rotation, i.e., 12345 -> 23451

def rotLeft(a, d):
    for i in range(d):
        temp = a.pop(0)
        a.append(temp)
    return a

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(result)

