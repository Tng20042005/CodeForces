t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    sum = 0
    check = 0
    c = 0
    for _ in range(n):
        a, b = map(int, input().split())    
        if check == b:
            if (a-c) % 2 != 0:
                sum += a - c - 1
            else:
                sum += a-c 
        else:
            if (a-c) % 2 != 0:
                sum += a - c
            else:
                sum += a- c -1
        check = b
        c = a
    sum += m - c
    print(sum)