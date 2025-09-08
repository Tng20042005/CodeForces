n = int(input())
lst_n = sorted(list(map(int, input().split())))
m = int(input())
lst_m = sorted(list(map(int, input().split())))

i_n = 0
i_m = 0
count = 0
while i_n < n and i_m < m:
    if abs(lst_n[i_n] - lst_m[i_m]) <= 1:
        count += 1
        i_n += 1
        i_m += 1
    else:
        if lst_n[i_n] > lst_m[i_m]:
            i_m+=1
        else:
            i_n+=1
print(count)
