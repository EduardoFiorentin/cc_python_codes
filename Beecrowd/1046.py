A, B = map(int, input().split())

if A == B: 
    hours = 24
elif A > B: 
    hours = (23 - A) + B + 1
elif A < B: 
    hours = B - A 

print(f"O JOGO DUROU {hours} HORA(S)") 