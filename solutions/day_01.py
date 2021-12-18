# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

from utils import get_input

# + [markdown] jp-MarkdownHeadingCollapsed=true tags=[] jp-MarkdownHeadingCollapsed=true jp-MarkdownHeadingCollapsed=true tags=[]
# ## Day 1
# -

content = get_input("day01.txt")

# ### part 1

# +
values = [int(i) for i in content.split("\n")]

previous_value = 999
increases = 0
for value in values:
    if value > previous_value:
        increases += 1
    previous_value = value

print(f"Solution is: {increases}")
# -

# ### part 2

# +
values = [int(i) for i in content.split("\n")]
triplet_sum = [sum(values[i:i+3]) for i,_ in enumerate(values)][:-2]

previous_value = 999
increases = 0
for value in triplet_sum:
    if value > previous_value:
        increases += 1
    previous_value = value

print(f"Solution is: {increases}")
