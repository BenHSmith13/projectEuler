__author__ = 'bensmith'

diagonals = 1
i = 2
sum = 1

while i < 1001:
    for j in range(0, 4):
        diagonals += i
        sum += diagonals
    i += 2

print(sum)