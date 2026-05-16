import math

def square(l):
    square = l**2
    return math.ceil(square)

l = float(input("Введите длину "))
result = square(l)
rounded = math.ceil(result)
print("l= ", l, "square =" , rounded)