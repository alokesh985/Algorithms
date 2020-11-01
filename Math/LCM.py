# We use gcd to find lcm

def gcd(x, y):
    if(x == 0):
        return y

    return gcd(y % x, x)

def lcm(x, y):
    return ((x * y) // gcd(x, y))

def main():

    ip = list(map(int, input("Enter numbers of which you want the LCM, seperated by a space: ").split()))
    
    if(len(ip) == 1):
        print(ip[0])


    elif(len(ip) == 2):
        print(lcm(ip[0], ip[1]))

    else:

        ans = lcm(ip[0], ip[1])

        for i in range(2, len(ip)):
            ans = lcm(ans, ip[i])
        
        print(ans)


if __name__ == "__main__":
    main()

