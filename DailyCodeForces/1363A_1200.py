t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    lst = list(map(int, input().split()))
    sum_even = 0
    sum_odd = 0
    for i in lst:
        if i % 2 == 0:
            sum_even+=1
        else:
            sum_odd+=1
    if sum_odd == 0:
        print("No")
    elif(x % 2 == 0 and sum_even == 0):
        print("No")
    elif x == n and sum_odd % 2 == 0:
        print("No")
    else:
        print("Yes")