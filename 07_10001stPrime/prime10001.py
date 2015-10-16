__author__ = 'Ben'

primes = []

for i in range(1, 1002, 2):
    while count < prime:
        if prime % count == 0:
            prime += 1
            count = 2
        else:
            count += 1
    print(prime, " : ", index)
    prime += 1
    count = 2

print(prime - 1)