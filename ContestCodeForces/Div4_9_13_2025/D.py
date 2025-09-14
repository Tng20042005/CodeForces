t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    
    odd = []
    total = 0
    for i in lst:
        if i % 2 == 0:
            total += i
        else:
            odd.append(i)
    
    odd = sorted(odd,reverse = True)
    if len(odd) == 0:
        print(0)
    else:
        if len(odd) % 2 == 0:
            total += sum(odd[:len(odd)//2])
        else:
            total += sum(odd[:(len(odd)+1)//2])
    
        print(total)
