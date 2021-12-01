from utils import get_input

content = get_input("day01a.txt")
values = [int(i) for i in content.split("\n")]

previous_value = 999
increases = 0
for value in values:
    if value > previous_value:
        increases += 1
    previous_value = value

print(f"Solution is: {increases}")
