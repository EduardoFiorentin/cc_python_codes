product1 = input()
product2 = input()

product1_list = product1.split()
product2_list = product2.split()

which_pay_prod1 = int(product1_list[1]) * round(float(product1_list[2]), 2)
which_pay_prod2 = int(product2_list[1]) * round(float(product2_list[2]), 2)

total_to_pay = round(which_pay_prod1 + which_pay_prod2, 2)

print(f"VALOR A PAGAR: R$ {total_to_pay:.2f}")