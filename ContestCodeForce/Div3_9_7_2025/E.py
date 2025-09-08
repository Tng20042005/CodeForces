t = int(input())

def mex(arr, n):
    seen = [False] * (n+1)
    for x in arr:
        if 0 <= x <= n:
            seen[x] = True
    for i in range(n+1):
        if not seen[i]:
            return i

for _ in range(t):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    for _ in range(min(k, n + 1)):  
        new_lst = []
        for i in range(n):
            tmp = lst[:i] + lst[i+1:]  
            new_lst.append(mex(tmp, n))
        if new_lst == lst:
            break
        lst = new_lst
    print(sum(lst))
