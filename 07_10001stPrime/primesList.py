__author__ = 'Ben'

primes = []

for i in range(3, 1000000, 2):
    primes.append(i)

for i in primes:
    for j in primes:
        if j > i and j % i == 0:
            primes.remove(j)

primes.insert(0, 2)
primes.insert(0, 1)
print(primes)