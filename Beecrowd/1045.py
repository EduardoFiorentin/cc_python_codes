A, B, C = map(float, input().split()) 

sort = [A, B, C] 
sort = sorted(sort)
A = sort[2] 
B = sort[1]
C = sort[0]

if A >= (B + C):
    print("NAO FORMA TRIANGULO")
else:
    if (A * A) == (B * B + C * C):
        print("TRIANGULO RETANGULO")
    if (A * A) > (B * B + C * C):
        print("TRIANGULO OBTUSANGULO")
    if (A * A) < (B * B + C * C): 
        print("TRIANGULO ACUTANGULO")
    if A == B == C: 
        print("TRIANGULO EQUILATERO")
    if A == B != C or A == C != B or B == C != A: 
        print("TRIANGULO ISOSCELES")