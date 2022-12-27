def prime(a, b):
    l = []
    for num in range(a, b + 1):
        if num > 1:                 # all prime numbers are greater than 1
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                l.append(num)
                for j in range(len(l)-1):
                    a = l.pop(j)
                    b = l.pop(j)
                    d = b - a - 1
                    print(f"{a} - {b} :", d)

a = int(input("first: "))
b = int(input("last: "))

print(prime(a, b))
