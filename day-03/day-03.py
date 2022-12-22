n = int(input("no. of numbers: "))

list = []
for x in range(1, n+1):
    list.append(int(input("number: ")))

a = 0
for y in range(len(list)):
	a = a + list[y]

avg = a/n

for z in range(len(list)):
		if list[z] > avg:
			print(list[z], end = " ")
