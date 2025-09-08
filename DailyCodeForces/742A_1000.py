n = int(input())
if n == 0 :
    print(1)
else:
    dic = {1:8, 2:4, 3:2,0:6}
    print(dic[n % 4])