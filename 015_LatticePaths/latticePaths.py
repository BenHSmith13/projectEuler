__author__ = 'bensmith'

lattice = []

for i in range(20):
    lattice.append([])

ct = 0
for i in range(20):
    for j in range(20):
        lattice[i].append(ct)
        ct += 1

adj = []

for i in range(400):
    adj.append([])

for i in range(20):
    for j in range(20):
        if j != 19:
            adj[lattice[i][j]].append(lattice[i][j+1])
        if i != 19:
            adj[lattice[i][j]].append(lattice[i+1][j])

q = [0]
ct = 0

while q:
    temp = q.pop(0)
    ct += 1
    i = 0
    while i < len(adj[temp]):
        q.append(adj[temp][i])
        i += 1

print(ct)