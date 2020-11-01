# This program will find the minimum number of elements in 's' such that the sum of any
# pair of elements is not evenly divisible by 'k'

def nonDivisibleSubset(k, s):
    
    # The count array will store the count of (each s) % k
    count = [0] * k

    for num in s:

        count[num % k] += 1


    # We can only take at max 1 element if number % k == 0. This is because if we take
    ans = min(1, count[0])

    # Let us take an example, say, k = 7. 6 + 1 = 7.
    # So for number % k == 1 or number % k == 6
    # We can only take one set of elements i.e., either the set with number % k == 6
    # or number % k == 1. We take the one with more number of elements.
    for i in range(1, len(count) // 2 + 1):

        if(i == (k - i)):
            ans += 1

        else:

            ans += max(count[i], count[k - i])

    return ans