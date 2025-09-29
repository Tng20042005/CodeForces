t = int(input())
for _ in range(t):
    n,x = map(int, input().split())
    lst = list(map(int, input().split()))
    if sum(lst) % x != 0:
        print(n)
        continue
    
    l = -1
    r = -1

    for i in range(n):
        if lst[i] % x != 0:
            l = i
            break
            
    for i in range(n - 1, -1, -1):
        if lst[i] % x != 0:
            r = i
            break
        
    if l == -1:
        print(-1)
    else:
        print(max(n - l - 1, r))