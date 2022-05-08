distance = int(input())

X_velocity = 60
Y_velocity = 90

'''
Dx = 60t
Dy = D + 90t
60t = D + 90t
D = 30t
t = D/30
'''

time = int((distance/30)*60)

print(time, "minutos")