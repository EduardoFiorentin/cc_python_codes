seller_name = input()
seller_fixed_salary = round(float(input()), 2)
seller_total_sales = round(float(input()), 2)

bonus_percentage = 15

seller_salary = seller_fixed_salary + (seller_total_sales * (bonus_percentage/100))

print(f"TOTAL = R$ {seller_salary:.2f}")