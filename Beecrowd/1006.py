A = round(float(input()), 1)
B = round(float(input()), 1)
C = round(float(input()), 1)

A_weight = 2
B_weight = 3
C_weight = 5

if A > 10 :
  A = 10.0

if B > 10 :
  B = 10.0

if C > 10 :
  C = 10.0

MEDIA = ((A*A_weight) + (B*B_weight) + (C*C_weight)) / (A_weight + B_weight + C_weight)

print(f"MEDIA = {MEDIA:.1f}")