value = int(input())

initial_value = value

hundred_notes = int(value/100)
value -= hundred_notes * 100

fifty_notes = int(value/50)
value -= fifty_notes * 50

twenty_notes = int(value/20)
value -= twenty_notes * 20

ten_notes = int(value/10)
value -= ten_notes * 10

five_notes = int(value/5)
value -= five_notes * 5

two_notes = int(value/2)
value -= two_notes * 2

one_notes = int(value/1)
value -= ten_notes * 1

print(initial_value)
print(hundred_notes, "nota(s) de R$ 100,00")
print(fifty_notes, "nota(s) de R$ 50,00")
print(twenty_notes, "nota(s) de R$ 20,00")
print(ten_notes, "nota(s) de R$ 10,00")
print(five_notes, "nota(s) de R$ 5,00")
print(two_notes, "nota(s) de R$ 2,00")
print(one_notes, "nota(s) de R$ 1,00")