def roman(num):
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    n_1000 = m[num // 1000]
    n_100 = c[(num % 1000) // 100]
    n_10 = x[(num % 100) // 10]
    n_1 = i[num % 10]

    rom = (n_1000 + n_100 + n_10 + n_1)
    return rom

if __name__ == "__main__":
    num = int(input("number: "))
    if num > 3999:
        print("number must be lesser than 3999")
    else:
        print(roman(num))
