# Input de valores
values = input()
values = values.split()

for index, position in enumerate(values): 
    values[index] = float(position) 
    
# verificação de quadrante
if values[0] == 0 and values[1] == 0: 
    print('Origem') 
else: 
    if values[0] == 0: 
        print('Eixo Y') 
    elif values[1] == 0: 
        print('Eixo X') 
    elif values[0] > 0: 
        if values[1] > 0: 
            print('Q1') 
        elif values[1] < 0: 
            print('Q4') 
    else: 
        if values[1] > 0: 
            print('Q2') 
        elif values[1] < 0: 
            print('Q3')