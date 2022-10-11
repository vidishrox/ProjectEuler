for t in range(int(input())):
    n = int(input())
    max = 0
    i = 100
    while i < 1000:
        j = i + 1
        while j < 1000:
            x = i * j
            z = x
            if x < n:
                y = 0
                while x != 0:
                    y = y * 10
                    y += x%10
                    x = x // 10
                if z == y and z > max:
                    max = z
    print(max)
