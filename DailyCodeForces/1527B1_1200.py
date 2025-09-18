t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    cnt0 = s.count("0")

    if cnt0 == 2 and n % 2 == 1 and s[n // 2] == '0':
        print("DRAW")
    elif cnt0 == 1:
        print("BOB")
    elif cnt0 % 2 == 1:
        print("ALICE")
    else:
        print("BOB")
