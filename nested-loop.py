# *
# **
# ***
# ****
# *****
for x in range(1,6):
    for a in range (x):
        print("*", end= " ")
    print()

# *****
# ****
# ***
# **
# *
for x in range(6,0,-1):
    for a in range(x):
        print("*", end=" ")
        print()
        


# 1
# 12
# 123
# 1234
# 12345

# 1
# 22
# 333
# 4444
# 55555

data = [
    [12, 34, 56, 78, 97],
    [23, 45, 67, 89, 90],
    [34, 56, 78, 90, 12]
]

sum_value = 0
total_even_number = 0
total_odd_number = 0

for row in data:
    for b in row:
        sum_value += b
        if b % 2 == 0:
            total_even_number += 1
        else:
            total_odd_number += 1

print("Sum of all values:", sum_value)
print("Total even numbers:", total_even_number)
print("Total odd numbers:", total_odd_number)