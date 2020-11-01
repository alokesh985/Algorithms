def fibonacci(x):
    ans = [0] * x
    ans[0] = 0
    ans[1] = 1

    for i in range(2, x):
        ans[i] = ans[i - 1] + ans[i - 2]

    return ans

def main():
    ip = int(input("Which Fibonacci number do you want to print? "))
    print(*fibonacci(ip))

if __name__ == "__main__":
    main()
    
    