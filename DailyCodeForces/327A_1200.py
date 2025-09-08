n = int(input())
a = list(map(int, input().split()))

total_ones = sum(a)

b = [1 if x == 0 else -1 for x in a]
best_gain = b[0]
current = b[0]
for i in range(1, n):
    current = max(b[i], current + b[i])
    best_gain = max(best_gain, current)

if total_ones == n:
    print(n - 1)
else:
    print(total_ones + best_gain)
