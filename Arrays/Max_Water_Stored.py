# Find the amount of water stored in between buildings of variable size
# Summation of (min(l(i), r(i)) - height(i)),     l(i) is the max height of building in left 
# r(i) is the max height of building in right

if __name__ == "__main__":
    ip = list(map(int, input().split()))

    left, right = [0] * len(ip), [0] * len(ip)

    maxi = ip[0]
    for i in range(len(ip)):
        if(ip[i] > maxi):
            maxi = ip[i]

        left[i] = maxi

    maxi = ip[len(ip) - 1]
    for i in range(len(ip) - 1, -1, -1):
        if(ip[i] > maxi):
            maxi = ip[i]

        right[i] = maxi

    ans = 0
    for i in range(len(ip)):
        ans += min(left[i], right[i]) - ip[i]

    print(ans)

    