p = int(input("Your First Number: "))
q = int(input("Your Last Number: "))

r = q + 1

if p >= q:
    print("The first number has to be smaller than the last number!!")
else:
    for x in range(p, r):
        if x%3 == 0:
            print("Foo")
        elif x%2 == 0 and (x%3 == 2 or x%3 == 1):
            print("Bar")
        else:
            print("Baz")