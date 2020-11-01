def SieveOfEratosthenes(num):
    # Initially all will be True as we are considering all of them to be prime
    prime_list = [True for number in range(num + 1)]

    pointer = 2

    while((pointer * pointer) <= num):
        # Checking the next unmarked (False) number
        if(prime_list[pointer] == True):

            # Make the values False that are multiples of p starting for p^2
            for i in range((pointer * pointer), num + 1, pointer):
                prime_list[i] = False

        pointer += 1

    # The values marked as True are prime
    return prime_list

def main():
    ip = int(input("Enter the Number upto which Prime Numbers will be printed: "))
    prime_list = SieveOfEratosthenes(ip)

    print(f"The Prime Numbers until {ip} are: ")

    # Printing the Prime Numbers
    for i in range(2, ip + 1):
        if(prime_list[i] == True):
            print(i, end = " ")

    print()

if __name__ == "__main__":
    main()
