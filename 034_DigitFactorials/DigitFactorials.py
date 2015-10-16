__author__ = 'bensmith'

import math

factorialSum = 0

for i in range(3, 10000000):
    digitSum = 0
    toString = str(i)
    for j in toString:
        digitSum += math.factorial(ord(j) - 48)
    if digitSum == i:
        factorialSum += i

print(factorialSum)