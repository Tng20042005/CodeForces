import math

def lcm(x, y):
    return x * y // math.gcd(x, y)

t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    
    a = n // lcm(x, y) 
    b = n // x - a      
    c = n // y - a      

    sum_b = (2*n - b + 1) * b // 2
    sum_c = c * (c + 1) // 2

    print(sum_b - sum_c)
