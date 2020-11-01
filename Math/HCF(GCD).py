def gcd(x, y):
    if(x == 0):
        return y

    return gcd(y % x, x)

if __name__ == '__main__':
    ip1, ip2 = map(int, input("Enter two Numbers: ").split())
    print(gcd(ip1, ip2))

# Alternate program
def gcd_alt(x, y):
    if(x == 0):
        return y

    if(y == 0):
        return x

    if(x > y):
        return gcd_alt(x - y, y)

    else:
        return gcd_alt(x, y - x)

# For n numbers, gcd(a,b,c) = gcd(a, gcd(b,c)) (Order does not matter)