for t in range(int(input())):
    n = int(input())
    m = n
    p = n
    sum = 0
    sum2 = 0
    if n % 3 != 0:
        n = n // 3
        sum = (n * (6 + (n - 1) * 3)) // 2
    elif n % 3 == 0:
        n = (n // 3) - 1
        sum = (n * (6 + (n-1) * 3)) // 2
    if m % 5 != 0:
        m = m // 5
        sum += (m * (10 + (m-1) * 5)) // 2
    elif m % 5 == 0:
        m = (m // 5) - 1
        sum += (m * (10 + (m-1) * 5)) // 2
    if p % 15 != 0:
        p = p // 15
        sum2=(p * (30 + (p-1) * 15)) // 2
    elif p %15 == 0:
        p = (p // 15) -1
        sum2=(p * (30 + (p-1) * 15)) // 2
    print (sum - sum2)
