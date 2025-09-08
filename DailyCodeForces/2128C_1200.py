t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    current_min = array[0]
    is_changable = True
    for value in array:
        if value < current_min:
            current_min = value
        elif value > current_min:
            res = value - current_min
            if res >= current_min:
                is_changable = False
                break
    if is_changable:
        print("YES")
    else:
        print("NO")