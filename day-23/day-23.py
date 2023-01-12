def revr(n):
    
    rev = 0
    while(n > 0):
        a = n % 10
        rev = rev * 10 + a
        n = n // 10
    
    return rev

num = int(input("Enter a number: "))
steps = 0

while steps<10:
    if num != revr(num):
        num += revr(num)
        steps += 1
        if steps == 500:
            print("too big")
            quit()
    else:
        break

print(num)
