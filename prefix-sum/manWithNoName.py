# Link: https://www.codechef.com/problems/BLONDIE

def findBulletsNeeded():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = []
    runningSum = 0
    for i in range(0, n):
        if arr[i] != -1:
            ans.append(arr[i])
            runningSum += arr[i]
        else:
            count = runningSum // i
            runningSum += count
            ans.append(count)
    print(*ans)

t = int(input())
for _ in range(t):
    findBulletsNeeded()
