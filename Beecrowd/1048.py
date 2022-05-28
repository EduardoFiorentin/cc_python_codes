A = float(input()) 

salary = A 
percentual = 0
money_earned = 0


if A <= 400:
    percentual = 0.15
elif A <= 800: 
    percentual = 0.12
elif A <= 1200: 
    percentual = 0.10
elif A <= 2000: 
    percentual = 0.07
else: 
    percentual = 0.04
    
print(f"Novo salario: {salary + (salary * percentual):.2f}")
print(f"Reajuste ganho: {percentual * salary:.2f}")
print(f"Em percentual: {int(percentual*100)} %")