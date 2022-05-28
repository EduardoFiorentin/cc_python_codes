num = int(input())

ins = 0
outs = 0

for num in range(0, num):
    inp = int(input())
    if 10 <= inp <= 20: 
        ins += 1
    else: 
        outs += 1 

print(f"{ins} in")
print(f"{outs} out")
