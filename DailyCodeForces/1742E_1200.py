import bisect

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    lst_n = list(map(int, input().split()))
    lst_q = list(map(int, input().split()))

    lst_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        lst_sum[i] = lst_sum[i - 1] + lst_n[i - 1]

    pref_max = [0] * n
    pref_max[0] = lst_n[0]
    for i in range(1, n):
        pref_max[i] = max(pref_max[i - 1], lst_n[i])

    result = []
    for x in lst_q:
        idx = bisect.bisect_right(pref_max, x)  
        result.append(str(lst_sum[idx]))
    print(" ".join(result))
