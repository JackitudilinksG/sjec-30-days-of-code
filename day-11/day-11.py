import math

c = float(input("Radius of circle: "))
s = float(input("Side of square: "))
t = float(input("Side of equilateral triangle: "))
r_a, r_b = map(float, input("Two sides of rectangle: ").split())

dict = {}
dict['circle'] = round(3.14*c*c, 2)
dict['square'] = round(s*s, 2)
dict['triangle'] = round((math.sqrt(3)*t*t)/4, 2)
dict['rectangle'] = round(r_a*r_b, 2)

#sorting
areas = [dict.get('circle'), dict.get('square'), dict.get('triangle'), dict.get('rectangle')]
areas.sort(reverse = True)

for i in range(len(areas)):
    d = areas.pop(0)
    print(list(dict.keys())[list(dict.values()).index(d)])
