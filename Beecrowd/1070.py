num = int(input())

odd = 0

while odd <= 6:
    if num % 2 != 0:
        print(num)
        odd += 1
    num += 1
    if odd == 6: 
        break 