# Link: https://www.geeksforgeeks.org/equilibrium-index-of-an-array/

# There is also a o(n^2) approach but here i have written o(n) solution
# Time: O(n) & Space: O(n) Where n is the length of the array
def equilibriumPoint(arr, n):
    if n == 1:
        return 0
    elif n == 2:
        return -1

    # When n >= 3
    prefix = [0] * (n+1)
    for i in range(1, n+1):
        prefix[i] = prefix[i-1] + arr[i-1]
    total = prefix[n]

    for i in range(1, n):
        leftSum = prefix[i+1] - arr[i]
        rightSum = total - prefix[i+1]

        if leftSum == rightSum:
            return i
    return -1

arr = [-7, 1, 5, 2, -4, 3, 0]
# arr = [1, 2, 6, 4, 0, -1]
# arr = [1, 2, 3]
n = len(arr)
print(equilibriumPoint(arr, n))
