value = int(input())

hours_passed = int(value / 3600)
value -= hours_passed * 3600

minutes_passed = int(value / 60)
value -= minutes_passed * 60

seconds_passed = int(value)


print(f"{hours_passed}:{minutes_passed}:{seconds_passed}")