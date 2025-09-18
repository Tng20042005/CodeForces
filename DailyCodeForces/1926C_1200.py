def digit_sum_upto(n: int) -> int:
    res = 0
    place = 1
    while place <= n:
        high = n // (place * 10)
        cur = (n // place) % 10
        low = n % place

        res += high * 45 * place
        res += (cur * (cur - 1) // 2) * place
        res += cur * (low + 1)

        place *= 10
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    print(digit_sum_upto(n))
