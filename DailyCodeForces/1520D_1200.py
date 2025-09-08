from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    b = [a[i] - i for i in range(n)]
    count = Counter(b)
    
    ans = 0
    for c in count.values():
        ans += c * (c - 1) // 2
    print(ans)
