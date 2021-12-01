from utils import get_input

content = get_input("day01a.txt")
values = [int(i) for i in content.split("\n")]
triplet_sum = [sum(values[i:i+3]) for i,_ in enumerate(values)][:-2]

previous_value = 999
increases = 0
for value in triplet_sum:
    if value > previous_value:
        increases += 1
    previous_value = value

print(f"Solution is: {increases}")
