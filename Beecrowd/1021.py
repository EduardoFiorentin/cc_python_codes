value = input()

value_list = value.split('.')

int_number = int(value_list[0])
dec_number = int(value_list[1])

hundred_notes = int_number // 100
int_number -= hundred_notes * 100

fifty_notes = int_number // 50
int_number -= fifty_notes * 50

twenty_notes = int_number // 20
int_number -= twenty_notes * 20

ten_notes = int_number // 10
int_number -= ten_notes * 10

five_notes = int_number // 5
int_number -= five_notes * 5

two_notes = int_number // 2
int_number -= two_notes * 2

'''====================== CENTS ======================='''

one_notes = int_number // 1
int_number -= one_notes * 1

fifty_cents = dec_number // 50
dec_number -= fifty_cents * 50

twenty_five_cents = dec_number // 25
dec_number -= twenty_five_cents * 25

ten_cents = dec_number // 10
dec_number -= ten_cents * 10

five_cents = dec_number // 5
dec_number -= five_cents * 5

one_cent = dec_number // 1
dec_number -= one_cent * 1

print("NOTAS:")
print(f"{hundred_notes} nota(s) de R$ 100.00")
print(f"{fifty_notes} nota(s) de R$ 50.00")
print(f"{twenty_notes} nota(s) de R$ 20.00")
print(f"{ten_notes} nota(s) de R$ 10.00")
print(f"{five_notes} nota(s) de R$ 5.00")
print(f"{two_notes} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{one_notes} moeda(s) de R$ 1.00")
print(f"{fifty_cents} moeda(s) de R$ 0.50")
print(f"{twenty_five_cents} moeda(s) de R$ 0.25")
print(f"{ten_cents} moeda(s) de R$ 0.10")
print(f"{five_cents} moeda(s) de R$ 0.05")
print(f"{one_cent} moeda(s) de R$ 0.01")