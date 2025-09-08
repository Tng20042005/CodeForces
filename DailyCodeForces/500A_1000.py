n, t = map(int, input().split())
lst = list(map(int, input().split()))
i = 0

while i < t-1:
    i+=lst[i]
print("YES" if i == t-1 else "NO")