# Link: https://codeforces.com/contest/1343/problem/D
from collections import defaultdict

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    prefix = [0] * (2 * k + 10)

    pairArr = [[min(arr[i], arr[n-i-1]), max(arr[i], arr[n-i-1])] for i in range(n//2)]

    keep = defaultdict(int)
    for i in range(len(pairArr)):
        l = pairArr[i][0] + 1
        r = pairArr[i][1] + k

        keep[pairArr[i][0] + pairArr[i][1]] += 1
        prefix[l] += 1
        prefix[r+1] -= 1
    s = 0
    for i in range(2*k+10):
        s += prefix[i]
        prefix[i] = s

    ans = float("inf")
    which_x = 0
    for x in range(2, 2*k+1):
        c0 = keep[x]
        c1 = prefix[x] - c0
        c2 = (n//2) - c1 - c0

        count = c2 * 2 + c1
        if ans > count:
            ans = count
            which_x = x
    print(ans)
