s = str(input())
kq = "hello"
index = 0
check = "NO"
for i in s:
    if i =='h'and index == 0:
        index+=1
    elif i == 'e' and index == 1:
        index+=1
    elif i == 'l' and (index == 2  or index == 3):
        index+=1
    elif i == 'o' and index ==4:
        check = 'YES'
        break
print(check)