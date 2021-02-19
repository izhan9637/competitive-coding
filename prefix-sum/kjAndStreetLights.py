# Link: https://www.hackerrank.com/contests/ab-yeh-kar-ke-dikhao/challenges/kj-and-street-lights/problem

n, p = map(int, input().split())
prefixArray = [0] * (p+1)

for i in range(n):
    temp = list(map(int, input().split()))
    l, r = temp[0], temp[1]
    if l - r >= 0:
        prefixArray[l-r] += 1
    else:
        prefixArray[0] += 1

    if l + r + 1 <= p:
        prefixArray[l+r+1] -= 1

for i in range(1, p+1):
    prefixArray[i] += prefixArray[i-1]

ans, count = float("-inf"), 0
for i in range(p+1):
    if prefixArray[i] != 1:
        count += 1
    else:
        ans = max(ans, count)
        count = 0
ans = max(ans, count)
print(ans)
