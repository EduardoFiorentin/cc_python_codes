#input de dados
data = input() 
data = data.split()
prices = [4, 4.5, 5, 2, 1.5] 

#variveis 
product_code = int(data[0])
product_quantity = int(data[1])

#calculo dos preços e retorno 
price = prices[product_code - 1] * product_quantity
print(f"Total: R$ {float(price):.2f}")
