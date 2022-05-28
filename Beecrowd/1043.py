#input de valores 
A, B, C = map(float, input().split()) 

#verificar se da pra fazer um triângulo 
    #lei de formação: 
    # | b - c | < a < b + c
    # | a - c | < b < a + c
    # | a - b | < c < a + b
triang_possivel = (B - C) < A < B + C and abs(A - C) < B < A + C and abs(A - B) < C < A + B
    

#se der: calcular o perímetro do triângulo (soma dos lados)
if triang_possivel: 
    print(f"Perimetro = {A + B + C:.1f}")    

#se não der: calcular a área do trapezio formado com bases AB e altura C
else: 
    print(f"Area = {(A+B)*C/2:.1f}")