t = int(input())

for _ in range(t):
    n = int(input())
    result = []
    for k in range(17, 0, -1):
        denominator = 1 + 10**k
        # print(n / denominator)
        if n % denominator == 0:
            result.append(int(n // denominator))
    print(len(result))
    if len(result) > 0:
        print(*result)