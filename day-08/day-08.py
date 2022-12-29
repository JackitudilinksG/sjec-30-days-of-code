m = int(input("Enter first number: "))
n = int(input("Enter second number: "))

if m == 1:
    m = m + 1
else:
    n = n + 1

if (m > 0 and n > 0 and m < n):
    for i in range(m, n+1):
        x = 1   #one interval
        for a in range(2, i):
            if i == 2 and a == 2:
                c = i
            elif (i % a) == 0:
                break
        else:
            c = i
            for j in range(i+1, n+1):
                for b in range(2, j):
                    if (j % b) == 0:
                        break
                else:
                    if x > 0:
                        x = x - 1
                        d = j
                        print(f'{c} - {d} : {(j - i - 1)}')
                        break
