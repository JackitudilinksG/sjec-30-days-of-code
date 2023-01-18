n = int(input("N: "))
m = int(input("M: "))

list = []
for i in range(n-1):
    list.append(0)
list.append(1)

while len(list)<m:
    num = 0
    for j in range(n):
        num += list[len(list)-1-j]
    list.append(num)

if m%10==1:
    print(f"{m}st number is {list[-1]}")
elif m%10==2:
    print(f"{m}nd number is {list[-1]}")
elif m%10==3:
    print(f"{m}rd number is {list[-1]}")
else:
    print(f"{m}th number is {list[-1]}")
