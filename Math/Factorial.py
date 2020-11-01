def fact(x):
    ans = 1
    for i in range(1, x + 1):
        ans *= i

    return ans

def main():
    ip = int(input("Enter the number whose factorial you want to print: "))
    print(fact(ip))

if __name__ == "__main__":
    main()