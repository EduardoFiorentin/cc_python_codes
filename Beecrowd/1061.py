x, dia0 = map(str, input().split()) 
hora0, minuto0, segundo0 = map(int, input().split(" : "))

y, dia1 = map(str, input().split()) 
hora1, minuto1, segundo1 = map(int, input().split(" : "))

init_time = int(dia0) * 86400 + hora0 * 3600 + minuto0 * 60 + segundo0
final_time = int(dia1) * 86400 + hora1 * 3600 + minuto1 * 60 + segundo1

total_time = final_time - init_time 

days = total_time // 86400 
total_time -= days * 86400

hours = total_time // 3600
total_time -= hours * 3600

minutes = total_time // 60
total_time -= minutes * 60
seconds = total_time

print(f"{days} dia(s)\n{hours} hora(s)\n{minutes} minuto(s)\n{seconds} segundo(s)")
