__author__ = 'bensmith'

lattice = []

for i in range(21):
    lattice.append([])

for i in range(21):
    for j in range(21):
            lattice[i].append(1)

for i in range(21):
    for j in range(21):
        if i != 0 and j != 0:
            lattice[i][j] = lattice[i - 1][j] + lattice[i][j -1]

print(lattice[20][20])