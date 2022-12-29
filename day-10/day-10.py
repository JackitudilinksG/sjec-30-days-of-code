import math

n = int(input("number: "))

a = math.factorial(n-10+4)
b = math.factorial(n-10)
factorial = a//(b*24)
print("total number of variations is:", factorial)
