n = int(input())
array = []

for _ in range(n):
    x = int(input())
    array.append(x)

array = sorted(array)

time_consume = 0
limit = n // 2 
l = 0
r = n - 1
while l <= r:
    if l != r:
        time_consume += array[l] * array[r] * 2
    else:
        time_consume += array[l] * array[r]
    time_consume %= 10007
    l += 1
    r -= 1
# for i in range(0, limit):
#     time_consume += array[i] * array[n - i - 1] * 2
#     # print(array[i], array[n - i - 1])
# if n % 2 == 1:
#     time_consume += array[n // 2] * array[n // 2]

print(time_consume % 10007)