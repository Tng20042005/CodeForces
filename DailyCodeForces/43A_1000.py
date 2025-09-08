x = int(input())
dic = {}
for _ in range(x):
    n = input()
    dic[n] = dic.get(n, 0) + 1
result = ""
m = 0
for i in dic:
    if dic[i] > m:
        m = dic[i]
        result = i
print(result)