def digit_sum_upto(n: int) -> int:
    """Sum of digits of all numbers from 1 to n inclusive."""
    if n <= 0:
        return 0
    # Based on the number of cycle
    res, power = 0, 1
    while power <= n:
        higher = n // (power * 10)
        curr = (n // power) % 10
        lower = n % power
        res += higher * 45 * power # full cycle
        res += curr * (lower + 1) # this digit
        res += (curr * (curr - 1) // 2) * power # digit < current contribution
        power *= 10
    return res

t = int(input())
d = {}
for i in range(1, 19):  # up to 18-digit blocks (since k ≤ 1e15)
    num_number = (10**i - 10**(i - 1))
    num_digits = i * num_number
    sum_digits = 45 * ((i-1) * 9 * 10**(i-2) + 10**(i-1)) if i > 1 else 45
    d[i] = (num_digits, sum_digits)

for _ in range(t):
    n = int(input())
    i = 1
    total = 0
    while n > 0:
        if n >= d[i][0]:
            n -= d[i][0]
            total += d[i][1]
            i += 1
        else:
            # Partial block
            n_number = n // i
            rest = n % i
            start = 10**(i - 1)
            if n_number > 0:
                total += digit_sum_upto(start + n_number - 1) - digit_sum_upto(start - 1)
            if rest > 0:
                next_num = start + n_number
                s = str(next_num)
                for j in range(rest):
                    total += int(s[j])
            break
    print(total)
