n = int(input("number of rows: "))
m = int(input("number of coloumns: "))

a = m*n

if m > 2 and n > 2:
    if m <= 0 or n <= 0:
            print("sides have to be positive")
    elif a%6 == 0:
        print("the grid will be covered")
    else:
        print("grid wont be covered")
else:
    print("minimum for both sides is 2")
