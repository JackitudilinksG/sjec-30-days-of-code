n = int(input("number of trees: "))
m = int(input("trees to pick from: "))
t = list(map(int, input("trees: ").split()))
t = t[:n]

b = []
for i in range(n-(m-1)):
    sum = 0
    for j in range(m):
        sum = sum + t[i+j]
    b.append(sum)

b.sort(reverse = True)
big = b.pop(0)
print("most cherries possible is", big)
