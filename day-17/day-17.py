n = int(input("number of frames: "))
f = list(map(int, input("frames: ").split()))
f = f[:n]

for i in range(n-1, -1, -1):
    if f[i] == f[i-1]:
        f.pop(i)
    
print(*f,sep=' ')
