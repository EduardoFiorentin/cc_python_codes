import math

point1 = input()
point2 = input()

point1_list = point1.split()
point2_list = point2.split()

X1 = round(float(point1_list[0]),1)
X2 = round(float(point2_list[0]),1)
Y1 = round(float(point1_list[1]),1)
Y2 = round(float(point2_list[1]),1)

Distance = math.sqrt(math.pow(X2 - X1, 2) + math.pow(Y2 - Y1, 2))

print(f"{Distance:.4f}")