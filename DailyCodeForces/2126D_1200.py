t = int(input())

for _ in range(t):
    n, coins = map(int, input().split())
    casinos = []
    for _ in range(n):
        l, r, real = map(int, input().split())
        casinos.append((l, r, real))
    
    sorted_casinos = sorted(casinos, \
        key=lambda r: (r[0]))
    for casino in sorted_casinos:
        # print(casino)
        l, r, real = casino
        if l <= coins and coins <= r and coins < real:
            coins = real
    print(coins)