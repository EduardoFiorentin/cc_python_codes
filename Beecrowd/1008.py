employees_number = int(input())
hours_worked = int(input())
amount_per_hour = float(input())

salary = round(hours_worked * amount_per_hour, 2)

print("NUMBER =", employees_number)
print(f"SALARY = U$ {salary:.2f}")