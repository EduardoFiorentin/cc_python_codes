import math

values = input()

values_list = values.split()

A = float(values_list[0])
B = float(values_list[1])
C = float(values_list[2])

delta = math.pow(B, 2) - (4 * A * C)

if delta <= 0 or A == 0 :
  print("Impossivel calcular")
else :
  root1 = (-B + math.sqrt(delta)) / (2 * A)
  root2 = (-B - math.sqrt(delta)) / (2 * A)
  print(f"R1 = {root1:.5f}")
  print(f"R2 = {root2:.5f}")