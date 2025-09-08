n, m =map(int, input().split())
emin = n
emax = n //2 if n % 2 == 0 else n//2 + 1
if emin < m:
    print(-1)
else:
    a = emax // m if emax % m == 0 else emax //m +1
    if a * m <= emin:
        print(a * m)
    else:
        print(-1)
    