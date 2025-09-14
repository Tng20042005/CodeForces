n = int(input())
lst = []
for _ in range(n):
    x = int(input())
    lst.append(x)
def dfs(i, total, n, arr):
    if i == n:
        return total % 360 == 0
    if dfs(i+1, total + arr[i],n, arr):
        return True
    if dfs(i+1, total - arr[i], n, arr):
        return True
    return False

total = 0
if dfs(0,0,n,lst):
    print("YES")
else:
    print("NO")