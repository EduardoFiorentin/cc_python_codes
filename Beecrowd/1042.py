# input 
values = input() 

# listagem
values = values.split() 
for index, value in enumerate(values): 
    values[index] = int(value) 

# ordenar 
sorted_values = sorted(values) 

#print
print(sorted_values[0])
print(sorted_values[1])
print(sorted_values[2])
print()
print(values[0])
print(values[1])
print(values[2])
