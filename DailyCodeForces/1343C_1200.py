t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    result = 0
    check = True if lst[0] > 0 else False
    m_d = float("-inf")
    m_a = float("-inf")
    for i in range(0,n):
        if lst[i] > 0:
            m_d = max(m_d, lst[i])
            if check == False:
                result += m_a
                m_a = float('-inf')
                check = True
        else:
            m_a = max(m_a, lst[i])
            if check == True:
                result += m_d
                m_d = float('-inf')
                check = False
        
    if check:
        result += m_d
    else:
        result += m_a
    print(result)

        
