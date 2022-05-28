salary = float(input())


if salary <= 2000: 
    print("Isento")
else: 
    if 3000 >= salary > 2000: 
        imposto = (salary - 2000) * 0.08
    elif salary <= 4500: 
        salary = salary - 2000
        imposto = (999.99 * 0.08) + (1499.99 * 0.18) + ((salary - 2499.98) * 0.18)
    else: 
        salary = salary - 2000
        imposto = (999.99 * 0.08) + (1499.99 * 0.18) + ((salary - 2499.98) * 0.28) 
    print(f"R$ {imposto:.2f}")