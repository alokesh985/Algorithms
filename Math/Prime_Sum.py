import math

def checkprime(x):
    prime = 1
    
    if x % 2 == 0:  # Even Number is never Prime
        return 0

# We are incrementing by 2 because we have considered the even number case above already.
# If we add 1 to an odd number, we will get an even number. So we are adding 2.

    root = math.floor(math.sqrt(x))
    for i in range(3, root + 1, 2): # Testing if number is prime
        if x % i == 0:              # Smaller factor is always <= sqrt(N), where N is the input
            prime = 0               # Larger Factor = (N / Smaller Factor)
            break
    
    return prime

def main():

    n = int(input())
    count = 0
    sum = 2

    for i in range(3, n, 2):

        flag = checkprime(i)
        if flag == 1:
            sum += i
            if sum >= n:
                break
            if checkprime(sum) == 1:
                count += 1
                # print('sum is ', sum)
    
    print(f"Inversions: {count}")

if __name__ == "__main__":
    main()
