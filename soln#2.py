arr = [1, 2, 3]

for t in range(int(input())):
    n = int(input())
    sum = 0
    i = 0
    while arr[i] <= n:
        if i == len(arr) - 1:
            arr.append(arr[-1] + arr[-2])
        if arr[i] % 2 == 0 and arr[i] <= n :
            sum += arr[i]
        i += 1
    print(sum)
