string = str(input("enter string: "))
high_string = string.upper()
x = high_string.split()
full_m = []

dict = {"A":".- ", "B":"-... ", "C":"-.-. ", "D":"-.. ", "E":". ", "F":"..-. ",
"G":"--. ", "H":".... ", "I":".. ", "J":".--- ", "K":"-.- " ,"L":".-.. ",
"M":"-- ", "N":"-. ", "O":"--- ", "P":".--. ", "Q":"--.- ", "R":".-. ",
"S":"... ", "T":"- ", "U":"..- ", "V":"...- ", "W":".-- ", "X":"-..- ",
"Y":"-.-- ", "Z":"--.. "}

for i in range(len(x)):
    m = x[i].translate(str.maketrans(dict))
    full_m.append(m)

print(*full_m, sep = '/ ')
