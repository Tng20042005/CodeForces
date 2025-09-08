t = int(input())

price = {}
for i in range(0, 20): 
    if i == 0:
        price[1] = 3 
    else:
        price[3**i] = 3**(i+1) + i * 3**(i-1)

for _ in range(t):
    n = int(input())
    total_cost = 0
    base = 0
    while n > 0:
        digit = n % 3
        if digit > 0:
            total_cost += digit * price[3**base]
        n //= 3
        base += 1
    print(total_cost)
