# bounce.py
#
# Exercise 1.5

height = 100.00
bounce = 0.6
i = 1

while i <= 10:
    height = height * bounce
    i = i + 1
    print(round(height, 4))
