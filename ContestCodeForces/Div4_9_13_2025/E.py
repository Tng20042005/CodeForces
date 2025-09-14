from collections import defaultdict

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Tổng số lần xuất hiện mỗi giá trị
    total_count = [0]*(n+1)
    for x in a:
        total_count[x] += 1
    
    # Nếu tổng count của một giá trị không chia hết cho k => không có subarray awesome
    impossible = any(c % k != 0 for c in total_count)
    if impossible:
        print(0)
        continue
    
    # Nếu tất cả count chia hết cho k, thì **mọi subarray đều awesome**
    # Có n*(n+1)//2 subarray
    print(n*(n+1)//2)
