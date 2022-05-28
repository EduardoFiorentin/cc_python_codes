A, B, C, D, E, F = input(), input(), input(), input(), input(), input()

values = [A, B, C, D, E , F]
sum_positives = 0
positives = 0 


for index, value in enumerate(values):
    value2 = float(value)
    if value2 > 0:
        positives += 1 
        sum_positives += value2 


print(f"{positives} valores positivos")
print(f"{sum_positives / positives:.1f}")
