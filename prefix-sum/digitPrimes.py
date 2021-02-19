# Link: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=1474

# Time complexity of this function: O(n*log(log(n)))
def generatePrime(n):
    prime = [False] * (n+1)

    # Make all odd numbers prime
    for i in range(3, n+1, 2):
        prime[i] = True

    for i in range(3, n+1, 2):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = False
    prime[2] = True
    prime[0], prime[1] = False, False
    return prime

n = 1000005
# Get all primes using Sieve of Eratosthenes
res = generatePrime(n)

def getDigitSum(number):
    s = 0
    for digit in str(number):
        s += int(digit)
    return s

# digitCount[i] will store the count of digit prime numbers from 0 to i.
digitCount = [0] * (n+1)
digitCount[2] = 1
for i in range(3, n+1):
    if res[i] and res[getDigitSum(i)]:
        digitCount[i] = digitCount[i-1] + 1
    else:
        digitCount[i] = digitCount[i-1]

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(digitCount[r] - digitCount[l-1])
