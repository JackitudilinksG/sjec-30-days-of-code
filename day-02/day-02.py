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
    elif (b>a and a>c) or (c>a and a>b):
        print(a)

def big(a, b, c):
    if a>b and a>c: #biggest
        print(a)
    elif b>a and b>c:
        print(b)
    elif c>a and c>b:
        print(c)

n = int(input("number of triangles: "))

l = {}
for x in range(1,n+1):       #adding into dictionary
    l[x] = []
    l[x].append(input("length of sides: "))

key = list(l.keys())

for y in range(len(key)):
    k = key.pop(0)
    q = l.get(k)
    while q != []:
        m = q.pop()
        a, b, c = m.split()
        if k%3 == 1:
            small(a, b, c)
        elif k%3 == 2:
            medium(a, b, c)
        elif k%3 == 0:
