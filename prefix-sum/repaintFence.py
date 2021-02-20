# Link: https://www.codechef.com/COOK56/problems/STRBIT

def repaintFence():
    n, k = map(int, input().split())
    s = str(input())
    prefix = [0] * (n+1)
    ans = 0
    for i in range(n):
        j = i - 1 if i-1 >= 0 else 0
        # Prefix[i] says that => from 0 to i prefix[i] flips has been made
        # It will indicate how many times a character has been flipped.
        prefix[i] += prefix[j]

        # if s[i] is "R" ans prefix[i] is even that means
        # s[i] has been flipped even times and when you flip R even times it will remain R
        # so in this case flip the required range and increase ans by 1
        if s[i] == "R" and prefix[i] % 2 == 0:
            ans += 1
            prefix[i] += 1
            right = i + k if i+k <=n else n
            prefix[right] -= 1
        # If s[i] is "G" and prefix[i] is odd then it means G has been flipped odd number of times.
        # for example if we flip G 3 times => G flip1 => R flip2 => G flip3 => R
        # That's why we need to flip this range
        elif s[i] == "G" and prefix[i] % 2:
            ans += 1
            prefix[i] += 1
            right = i + k if i+k <=n else n
            prefix[right] -= 1
    print(ans)



t = int(input())
for _ in range(t):
    repaintFence()
