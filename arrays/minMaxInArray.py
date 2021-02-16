# Link: https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/

# Comparisons => 2 * (n-2) + 1
def findMinMax_MethodOne(arr):
    n = len(arr)
    if n == 1:
        minimum = arr[0]
        maximum = arr[0]
    else:
        if arr[0] < arr[1]:
            minimum = arr[0]
            maximum = arr[1]
        else:
            minimum = arr[1]
            maximum = arr[0]
        for i in range(2, n):
            if arr[i] < minimum:
                minimum = arr[i]
            if arr[i] > maximum:
                maximum = arr[i]
    print(minimum, maximum)

# Optimised Approach
# Comparisons when n is EVEN => 3 * (n-2) / 2 + 1
# Comparisons when n is ODD  => 3 * (n-1) / 2
def findMinMax_MethodTwo(arr):
    n = len(arr) - 1
    if n % 2 == 0:
        if arr[0] < arr[1]:
            minimum = arr[0]
            maximum = arr[1]
        else:
            minimum = arr[1]
            maximum = arr[0]
        i = 2
    else:
        minimum = arr[0]
        maximum = arr[0]
        i = 1

    while i < n:
        if arr[i+1] > arr[i]:
            if arr[i+1] > maximum:
                maximum = arr[i+1]
            if arr[i] < minimum:
                minimum = arr[i]
        else:
            if arr[i] > maximum:
                maximum = arr[i]
            if arr[i+1] < minimum:
                minimum = arr[i+1]
        i += 2
    print("Min Value:", minimum, "Max Value:", maximum)
arr = [2, 5, -1, 6, 3, 4]
findMinMax_MethodTwo(arr)
