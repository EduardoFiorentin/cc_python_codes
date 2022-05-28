# input
A, B, C, D = map(float, input().split())

#calcular média com pesos 2, 3, 4 e 1
media = ((A * 2) + (B * 3) + (C * 4) + D) / 10

print(f"Media: {media:.1f}")

# nota 7 ou mais - aprovado 
if media >= 7: 
    print("Aluno aprovado.")

# menos do que 5 - reprovado 
elif media < 5:
    print(f"Aluno reprovado.")

# entre 5 e 6.9 (inclusos) - recuperação 
else: 
    
    # exame: print de exame e ler mais um valor
    print("Aluno em exame.")
    nova_nota = float(input())
    print(f"Nota do exame: {nova_nota:.1f}")
    
    # nova média - media da nova nota com a média antiga
    nova_media = (media + nova_nota) / 2
    
    #nova média 5 ou mais: aprovado, 4.9 ou menos: reprova
    if nova_media >= 5: 
        print("Aluno aprovado.")
        print(f"Media final: {nova_media:.1f}")
    else: 
        print("Aluno reprovado.")
        print(f"Media final: {nova_media:.1f}")