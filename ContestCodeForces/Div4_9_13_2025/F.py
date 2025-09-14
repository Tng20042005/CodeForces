t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        lst = list(map(int, input().split()))
        arr.append(lst[1:])

    # Sắp xếp các mảng theo phần tử đầu tiên
    arr.sort(key=lambda x: x[0])

    # Hàng dưới cùng = nối các mảng sau khi sort
    base = arr[0]
    for i in range(1, n):
        if len(arr[i]) > len(base):
            base.extend(arr[i][len(base):])

    print(" ".join(map(str, base)))
