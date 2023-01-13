from random import shuffle

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

shf = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

shuffle(shf)
dic = (list(zip(alpha,shf)))

for i in range(len(dic)):                 #no remap
    if dic[i][0] == dic[i][1]:
        shuffle(shf)
        dic = (list(zip(alpha,shf)))

string = str(input("string: "))
low_str = string.lower()
dic = dict(dic)                    #maping

tra = low_str.translate(str.maketrans(dic))
words = tra.split()

freq = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}

for word in words:
    for letter in word:
        if letter in freq:
            freq[letter] += 1

top = sorted(freq.items(), key=lambda x: x[1], reverse=True)

eng_freq = ['e', 'a', 'r', 'i', 'o', 't', 'n', 's', 'l', 'c', 'u', 'd', 'p', 'm', 'h', 'g', 'b', 'f', 'y', 'w', 'k', 'v', 'x', 'z', 'j', 'q']

new_dict = [ (o, eng) for (o, _), eng in zip(top, eng_freq)]
new_dict = dict(new_dict)

tra_2 = tra.translate(str.maketrans(new_dict))
print(tra_2)
