t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    current_threshold = 0
    count = 0
    for value in array:
        if value > current_threshold:
            current_threshold = value + 1
            count += 1
    print(count)