x1, y1, x2, y2 = map(int, input().split())

if x1 == x2:  # cùng cột
    d = abs(y1 - y2)
    x3, y3 = x1 + d, y1
    x4, y4 = x2 + d, y2
    print(x3, y3, x4, y4)
elif y1 == y2:  # cùng hàng
    d = abs(x1 - x2)
    x3, y3 = x1, y1 + d
    x4, y4 = x2, y2 + d
    print(x3, y3, x4, y4)
elif abs(x1 - x2) == abs(y1 - y2):  # chéo → hình vuông
    x3, y3 = x1, y2
    x4, y4 = x2, y1
    print(x3, y3, x4, y4)
else:
    print(-1)
