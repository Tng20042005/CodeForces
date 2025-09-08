a,b = map(int, input().split())
count = 0
i = 1
while i * i <= b and i <= a:
    if b % i == 0 and b/i <= a:
        if b / i != i:
            count += 2
        else:
            count +=1 
    i += 1
print(count)