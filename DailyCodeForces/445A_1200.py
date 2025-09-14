n, m = map(int, input().split())
for i in range(n):
    s = input().strip()
    result = ""
    for j in range(m):
        if s[j] == ".":
            if (i + j) % 2 == 0:
                result += "B"
            else:
                result += "W"
        else:
            result += "-"
    print(result)
