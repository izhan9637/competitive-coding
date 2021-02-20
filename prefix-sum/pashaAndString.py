# Link: https://codeforces.com/contest/525/problem/B

s = list(str(input()))
m = int(input())
arr = list(map(int, input().split()))
n = len(s)
prefix = [0] * (n+1)
mid = n // 2
for i in range(m):
    left = arr[i] - 1
    right = n - left - 1
    prefix[left] += 1
    prefix[right+1] -= 1

for i in range(1, mid + 1):
    prefix[i] += prefix[i-1]

for i in range(mid):
    # If prefix[i] is even then then it means no reversing.
    # because reversing even number of times is no reversing.
    if prefix[i] % 2 != 0:
        s[i], s[n-i-1] = s[n-i-1], s[i]
print("".join(s))
