t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())
    a = list(map(int, input().split()))  # tọa độ các tia ngang
    b = list(map(int, input().split()))  # tọa độ các tia dọc
    sum = 0
    for i in a:
        if y >= i:
            sum += 1
        else:
            break
    for i in b:
        if x >= i:
            sum += 1
        else:
            break
    print(sum)