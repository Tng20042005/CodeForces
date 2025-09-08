t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    groups = {}
    for i, val in enumerate(b):
        groups.setdefault(val, []).append(i)

    ok = True
    a = [0] * n
    cur = 1  

    for val, idxs in groups.items():
        if len(idxs) % val != 0:
            ok = False
            break
        for i in range(0, len(idxs), val):
            for j in idxs[i:i+val]:
                a[j] = cur
            cur += 1

    if not ok:
        print(-1)
    else:
        print(" ".join(map(str, a)))
