__author__ = 'bensmith'

sums = 0

for i in range(1, 1001):
    sums += i ** i

toString = str(sums)

for i in range(len(toString)-10, len(toString)):
    print(toString[i], end="")