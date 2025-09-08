
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    prefix = [0] * (n+1)
    suffix = [0] * (n+1)

    seen = set()
    for i in range(n):
        seen.add(s[i])
        prefix[i+1] = len(seen)

    seen.clear()
    for i in range(n-1, -1, -1):
        seen.add(s[i])
        suffix[i] = len(seen)

    ans = 0
    for i in range(1, n):
        ans = max(ans, prefix[i] + suffix[i])

    print(ans)
