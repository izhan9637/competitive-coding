# Link: https://www.spoj.com/problems/CSUMQ/

n = int(input())
arr = list(map(int, input().split()))
cumulativeSumArray = [0] * (n+1)

for i in range(1, n+1):
    cumulativeSumArray[i] = cumulativeSumArray[i-1] + arr[i-1]

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(cumulativeSumArray[r+1] - cumulativeSumArray[l])
