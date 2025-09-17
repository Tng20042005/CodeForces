import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    cnt = {}
    for x in arr:
        msb = x.bit_length() - 1 
        cnt[msb] = cnt.get(msb, 0) + 1
    
    ans = 0
    for c in cnt.values():
        ans += c * (c - 1) // 2
    print(ans)
