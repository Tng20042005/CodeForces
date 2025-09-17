t = int(input())

for _ in range(t):
    n = int(input())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    lst3 = list(map(int, input().split()))

    r1 = sorted([(val, i) for i, val in enumerate(lst1)], reverse=True)[:3]
    r2 = sorted([(val, i) for i, val in enumerate(lst2)], reverse=True)[:3]
    r3 = sorted([(val, i) for i, val in enumerate(lst3)], reverse=True)[:3]

    ans = 0
    for v1, i1 in r1:
        for v2, i2 in r2:
            for v3, i3 in r3:
                if i1 != i2 and i2 != i3 and i3 != i1:
                    ans = max(ans, v1 + v2 + v3)
    print(ans)
