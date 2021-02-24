# Link: https://www.spoj.com/problems/AGGRCOW/


t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    arr.sort()
    low, high = 0, arr[n-1]
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        # print(low, high, mid)
        cow, prev = 1, arr[0]
        for i in range(1, n):
            if arr[i] - prev >= mid:
                # print("IN ", prev, arr[i])
                cow += 1
                prev = arr[i]
                if c == cow:break

        if cow == c:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    print(ans)
