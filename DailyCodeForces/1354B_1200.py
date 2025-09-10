t = int(input())
for _ in range(t):
    s = input()
    count = {}
    result = float("inf")
    l = 0
    for r in range(len(s)):
        if s[r] not in count:
            count[s[r]] = 1
        else:
            count[s[r]] += 1

        while len(count) == 3:
            result = min(result, r - l + 1)
            count[s[l]] -= 1
            if count[s[l]] == 0:
                del count[s[l]]
            l += 1
    print(0 if result == float('inf') else result)
