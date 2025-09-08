t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a, b = map(int, input().split())
    c = min(n,m)
    d = max(n,m)
    if a * 2 < b:
        print((c+d)*a)
    else:
        print(c * b + (d-c) * a)