__author__ = 'bensmith'

powers = []

for i in range(2, 101):
    for j in range(2, 101):
        if i ** j not in powers:
            powers.append(i ** j)

print(len(powers))