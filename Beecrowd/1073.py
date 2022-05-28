#ler um valor 
num = int(input())

#printar o quadrado de cada um dos números pares entre 0 e o valor 
for number in range(1, num+1): 
    if number % 2 == 0:
        print(f"{number}^2 = {number * number}")
