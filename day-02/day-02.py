def small(a, b, c):
    if a>c and b>c:
        print(c)
    elif a>b and c>b:
        print(b)
    else:
        print(a)

def medium(a, b, c):
    if (a>c and c>b) or (b>c and c>a):
        print(c)
    elif (a>b and b>c) or (c>b and b>a):
        print(b)
    else:
        print(a)

def big(a, b, c):
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    else:
        print(c)

n = int(input("number of triangles: "))

l = {}
for x in range(1,n+1):
    l[x] = []
    l[x].append(input("length of sides: "))

key = list(l.keys())

for y in range(n):
    k = key.pop(0)
    q = l.get(k)
    while q != []:
        m = q.pop()
        a, b, c = m.split()
        if k%3 == 1:
            small(a, b, c)
        elif k%3 == 2:
            medium(a, b, c)
        else:
            big(a, b, c)
