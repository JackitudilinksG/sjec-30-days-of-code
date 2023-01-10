f = int(input("first number of range: "))
l = int(input("last number of range: "))

steps = []
dict = {}
num = []

for x in range(f, l+1):
    num.append(x)

for i in range(f,l+1):
    n = 0
    while i != 1:
        if i%2 == 0:
            i = i/2
            n += 1
        else:
            i = 3*i + 1
            n += 1
    steps.append(n+1)

for j in range(l-f+1):
    dict[j] = steps[(j)]

steps.sort(reverse = True)
a = (list(dict.keys())[list(dict.values()).index(steps[0])])
print(num[a], "has the most number of steps")
