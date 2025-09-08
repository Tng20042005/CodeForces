from math import sqrt
r = int(input())

numerator = r - 1
limit = int(sqrt(numerator))
# print(limit)
find_flag = False
for x in range(1, limit + 1):
    if numerator % x != 0:
        continue
    y_raw = numerator / x - x - 1
    # print(y_raw)
    if y_raw > 0 and y_raw % 2 == 0:
        print(x, int(y_raw / 2))
        find_flag = True
        break

if not find_flag:
    print('NO')
