A, B, C, D = map(int, input().split()) 
time = [0, 0]

# if A == -1: 
#     break

# A == C 
if A == C: 
    #se B = D - 24 horas cravado 
    if B == D: 
        time = [24, 0]

    #se B != D - 23 horas e alguma coisa (B > D - obrigatório)
    else: 
        if B > A: 
            time = [23, ((60 - B) + D)]
        else: 
            time = [0, D - B]

# A < C - mesmo dia (menos de 24 horas) 
elif A < C:
    #Horas : C - A
    time = [C - A, 0]

    # Minutos: 
    # B > D: (60 - B) + D -> B até 60 mais o C
    if B > D: 
        hora = time[0] - 1
        time = [hora, (60 - B) + D]

        # B <= D: D - B
    if B <= D: 
        time[1] = ((60 - B) + D) - 60


# A > C - dias diferentes obrigatoriamente 
elif A > C:
    #horas: (24 - A) + C
    time = [(24 - A) + C, 0]

    # B > D: (60 - B) + D -> B até 60 mais o C
    if B > D: 
        hora = time[0] - 1
        time = [hora, (60 - B) + D]

        # B <= D: D - B
    if B <= D: 
        time[1] = ((60 - B) + D) - 60
    


print(f"O JOGO DUROU {time[0]} HORA(S) E {time[1]} MINUTO(S)")