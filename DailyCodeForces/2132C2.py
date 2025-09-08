t = int(input())

price_dict = {}
for i in range(0, 17):
    price_dict[3 ** i] = 3 ** (i + 1) + i * 3 ** (i - 1)

# for w in price_dict.keys():
#     print(w, price_dict[w])
for _ in range(t):
    n, k = map(int, input().split())
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for melon in range(n + 1):
        for deal in range(k + 1):
            if dp[melon][deal] != float('inf'):
                for w in price_dict.keys():
                    if melon + w <= n and deal + 1 <= k:
                        dp[melon + w][deal + 1] = min(dp[melon + w][deal + 1],\
                            dp[melon][deal] + price_dict[w])
                    # else:
                    #     break

    ans = min(dp[n][d] for d in range(k + 1))
    if ans == float('inf'):
        print(-1)
    else:
        print(int(ans))
    