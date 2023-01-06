def returnSum(dict):

    sum = 0
    for quack_1 in dict:
        sum = sum + dict[quack_1]

    return sum

string = str(input("string: "))
low_str = string.lower()
words = low_str.split()
letters = []

alpha = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}

for word in words:
    for letter in word:
        if letter in alpha:
            alpha[letter] += 1

top = sorted(alpha.items(), key=lambda x: x[1], reverse=True)

counter = 0

total = returnSum(alpha)

for key, val in top:
    print(f"{key} - {round((val/total)*100, 1)}%")
    counter += 1
    if counter == 5:
        break
