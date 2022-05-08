A = round(float(input()), 2)
B = round(float(input()), 2)

A_weight = 3.5
B_weight = 7.5

MEDIA = ((A*A_weight) + (B*B_weight)) / (A_weight + B_weight)

print(f"MEDIA = {MEDIA:.5f}")