t = int(input())
for _ in range(t):
    n = int(input())
    lst = sorted(list(map(int, input().split())))
    
    l = 0
    m = lst[1] - lst[0]
    for i in range(1, n - 1):
        if lst[i+1] - lst[i] < m:
            m = lst[i+1] - lst[i]
            l = i
    
    result = [lst[l]]
    result.extend(lst[l+2:])  
    result.extend(lst[:l])    
    result.append(lst[l+1])  
    
    print(*result)
