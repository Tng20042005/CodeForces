n = str(input())
result = ""
for i in n:
    if len(result) == 0 and i == "9":
        result += i
    else:
        result += str(min(int(i), 9 - int(i)))
print(result)