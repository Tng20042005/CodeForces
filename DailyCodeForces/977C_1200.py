n, k = map(int, input().split())
lst = sorted(map(int, input().split()))

if k == 0:
    if lst[0] > 1:
        print(lst[0] - 1)
    else:
        print(-1)
elif k == n:
    print(lst[-1])
else:
    if lst[k-1] < lst[k]:
        print(lst[k-1])
    else:
        print(-1)
