from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    freq = Counter(lst)
    ans = 0

    for s in range(2, 2*n + 1):
        cnt = 0
        for x in freq:
            y = s - x
            if y in freq:
                if x == y:
                    cnt += freq[x]//2
                elif x < y:
                    cnt += min(freq[x], freq[y])
        ans = max(ans, cnt)
    print(ans)