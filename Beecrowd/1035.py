numbers = input()

number_list = numbers.split()

A = int(number_list[0])
B = int(number_list[1])
C = int(number_list[2])
D = int(number_list[3])

CD = C + D
AB = A + B

if (B>C and D>A and CD>AB and C>=0 and D>=0 and A%2 == 0) :
  print("Valores aceitos")
else :
  print("Valores nao aceitos")
