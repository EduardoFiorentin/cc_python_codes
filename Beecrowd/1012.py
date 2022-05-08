import math

data = input()
data_list = data.split()

A = float(data_list[0])
B = float(data_list[1])
C = float(data_list[2])

pi = 3.14159

triangule_area = (A * C) / 2
circle_area = pi * math.pow(C, 2)
trapezium_area = ((A + B) * C) / 2
square_area = math.pow(B, 2)
rectangle_area = A * B

print(f"TRIANGULO: {triangule_area:.3f}")
print(f"CIRCULO: {circle_area:.3f}")
print(f"TRAPEZIO: {trapezium_area:.3f}")
print(f"QUADRADO: {square_area:.3f}")
print(f"RETANGULO: {rectangle_area:.3f}")