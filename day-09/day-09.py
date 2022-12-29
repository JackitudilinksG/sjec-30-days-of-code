n = int(input("Enter the width of diamond: "))
n = n-1
for i in range(n):
    for j in range(n - i):
        print(end=" ")

    for j in range(i + 1):
        print(end=" #")
    print()

for i in range(n, -1, -1):
    for j in range(n - i):
        print(end=" ")

    for j in range(i + 1):
        print(end=" #")
    print()
