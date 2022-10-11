for t in range(int(input())):
    n = int(input())
    i = 2
    max = 0
    while i <= n ** 0.5:
        if n % i == 0:
            while n % i == 0:
                n = n // i
        if i > max:
            max = i
        i += 1
    if n != 1:
        max = n
    print(max)
