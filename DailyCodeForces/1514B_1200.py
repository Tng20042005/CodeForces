MOD = 10**9 + 7

t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().split())
    print(pow(n, k, MOD))
