final = int(input())
initial = int(input())

initial += 1


soma = 0
while initial <= final: 
    if initial % 2 != 0:
#        if initial > 0:
        soma += initial
    initial += 1
    if initial == final:
        break

print(soma)