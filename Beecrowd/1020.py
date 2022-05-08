value = int(input())

years_passed = int(value / 365)
value -= years_passed * 365

months_passed = int(value / 30)
value -= months_passed * 30

days_passed = int(value)

print(years_passed, "ano(s)")
print(months_passed, "mes(es)")
print(days_passed, "dia(s)")