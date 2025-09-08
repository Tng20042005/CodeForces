t = int(input())

for _ in range(t):
    n = int(input())
    a = input()
    m = int(input())
    b = input()
    c = input()

    i = 0
    for char in c:
        if char == 'D':
            a = a + b[i]
        else:
            a = b[i] + a
        i += 1

    print(a)