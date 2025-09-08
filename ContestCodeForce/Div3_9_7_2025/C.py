t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    candidates = []

    # k = 1
    if (a + b) % 2 == 0:
        candidates.append(a + b)

    # k = b
    if (a * b + 1) % 2 == 0:
        candidates.append(a * b + 1)

    # k = 2 nếu b chẵn
    if b % 2 == 0:
        val1 = 2 * a + b // 2
        c = b /2 
        val2 = c * a + 2
        if val1 % 2 == 0:
            candidates.append(val1)
        if val2 % 2 == 0:
            candidates.append(val2)

    if candidates:
        print(int(max(candidates)))
    else:
        print(-1)
