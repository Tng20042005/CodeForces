import bisect

n = int(input())
sl_lst = list(map(int,input().split()))
k = int(input())
i_lst = list(map(int, input().split()))
sum = 0
lst = [0] * (n + 1)
for i in range(1,n+1):
    lst[i] += lst[i-1] + sl_lst[i-1]

for i in i_lst:
    print(bisect.bisect_left(lst,i))
    