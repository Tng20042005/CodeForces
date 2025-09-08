import math

def solve(n, k):
    S = math.ceil(n / k) * k
    return math.ceil(S / n)

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(solve(a,b))
