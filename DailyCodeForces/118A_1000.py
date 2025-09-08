s = str(input())
lst = ["A", "O", "Y", "E", "U", "I"]
result = ""
for i in s:
    if i.upper() not in lst:
        result += "." + i.lower()
print(result)