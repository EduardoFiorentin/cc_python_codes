spent_time = int(input())
average_speed = int(input())

fuel_spent_per_km = 12

''' V = S/T -> S = VT '''

distance = average_speed * spent_time
comsuption = distance / fuel_spent_per_km

print(f"{comsuption:.3f}")