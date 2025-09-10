t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    lst = [0] + lst
    count = 0
    for i in range(1, n+1):
        max_k = 2*n // lst[i] + 1
        for k in range(1, max_k + 1):
            j = k * lst[i] - i
            if j > i and j <= n :
                if lst[i] * lst[j] == i + j:
                    count+=1
    
    print(count)