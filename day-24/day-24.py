from random import shuffle

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

shf = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

shuffle(shf)
dic = (list(zip(alpha,shf)))

for i in range(len(dic)):                 #no remap
    if dic[i][0] == dic[i][1]:
        shuffle(shf)
        dic = (list(zip(alpha,shf)))
        
string = str(input("sentence: "))
dic = dict(dic)
print(string.translate(str.maketrans(dic)))
