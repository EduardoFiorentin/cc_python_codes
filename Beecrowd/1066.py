A, B, C, D, E =  input(), input(), input(), input(), input()

values = [A, B, C, D, E]

even = 0
odd = 0
positive = 0 
negative = 0

for value in values: 
    value = int(value) 
    
    if value % 2 == 0:
        even += 1
    else: 
        odd += 1
    if value > 0: 
        positive += 1
    if value < 0: 
        negative += 1
        
print(f"{even} valor(es) par(es)\n{odd} valor(es) impar(es)\n{positive} valor(es) positivo(s)\n{negative} valor(es) negativo(s)")