value = float(input())  #input do valor inicial em reais

values = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.10, 0.05, 0.01]
num_notes =[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]

for index, nota in enumerate(values):
    if nota <= value: 
        notas = value // values[index]
        num_notes[index] = int(notas)
        value -= nota * notas
        if value < 0.05:
            value = round(value, 2)
            while (value > 0):
                num_notes[11] += 1
                value -= 0.01




#Apresentação dos valores
print('NOTAS:')
print(f"{num_notes[0]} nota(s) de R$ 100.00")
print(f"{num_notes[1]} nota(s) de R$ 50.00")
print(f"{num_notes[2]} nota(s) de R$ 20.00")
print(f"{num_notes[3]} nota(s) de R$ 10.00")
print(f"{num_notes[4]} nota(s) de R$ 5.00")
print(f"{num_notes[5]} nota(s) de R$ 2.00")
print('MOEDAS:')
print(f"{num_notes[6]} moeda(s) de R$ 1.00")
print(f"{num_notes[7]} moeda(s) de R$ 0.50")
print(f"{num_notes[8]} moeda(s) de R$ 0.25")
print(f"{num_notes[9]} moeda(s) de R$ 0.10")
print(f"{num_notes[10]} moeda(s) de R$ 0.05")
print(f"{num_notes[11]} moeda(s) de R$ 0.01")

