n, t = map(int, input().split())
s_e = "1" + '0' * (n-1)
e_e = "9" * n
a = int(s_e) // t if int(s_e) % t == 0 else int(s_e) // t + 1
if a * t <= int(e_e):
    print(a * t)
else:
    print(-1) 