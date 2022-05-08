values = input()
values_list = values.split()

A = int(values_list[0])
B = int(values_list[1])
C = int(values_list[2])

Greater_btw_AB = int((A + B + abs(A-B)) / 2)
Greater_btw_XC = int((Greater_btw_AB + C + abs(Greater_btw_AB - C)) / 2)
  
print(Greater_btw_XC, "eh o maior")