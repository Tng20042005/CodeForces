t = int(input())
for _ in range(t):
    total = 0
    n = int(input())
    s = input()
    lst = []
    for i in s:
        if i == "(":
            lst.append(i)
        else:
            if len(lst) != 0:
                lst.pop(0)
            else:
                total +=1
    print(total)