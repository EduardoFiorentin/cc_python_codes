A, B, C, D, E =  input(), input(), input(), input(), input()

values = [A, B, C, D, E]

evens = 0

for value in values: 
    value2 = int(value)
    if value2 % 2 == 0:
        evens += 1

print(f"{evens} valores pares")