t = int(input())
for _ in range(t):
    n = int(input())
    x = input()
    a = ""
    b = ""
    check = False
    for i in range(n):
        if x[i] == "0":
            a += "0"
            b += '0'
        elif x[i] == "2":
            if check == False:
                a += '1'
                b += '1'
            else:
                a += "0"
                b += "2"
        else:
            if check == False:
                a += "1"
                b += '0'
                check = True
            else:
                a += '0'
                b += '1'

    print(a)
    print(b)