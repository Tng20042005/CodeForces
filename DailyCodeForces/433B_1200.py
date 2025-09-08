n = int(input())
lst = list(map(int, input().split()))
s_lst = sorted(lst)
m = int(input())
sum_lst = [0] * (n+1)
sum_s_lst = [0] * (n +1)
for i in range(1, n+1):
    sum_lst[i] = sum_lst[i-1] + lst[i-1]
    sum_s_lst[i] = sum_s_lst[i-1] + s_lst[i-1]
for _ in range(m):
    t, l, r = map(int, input().split())
    if t == 1:
        print(sum_lst[r] - sum_lst[l-1])
    else:
        print(sum_s_lst[r] - sum_s_lst[l-1])