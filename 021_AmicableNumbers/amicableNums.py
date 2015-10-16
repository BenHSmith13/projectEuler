__author__ = 'bensmith'

amicableSum = 0

for i in range(2, 10000):
    divisorSum = 0
    divisorSum2 = 0
    for j in range(1, i):
        if i % j == 0:
            divisorSum += j
    if divisorSum != i:
        for j in range(1, divisorSum):
            if divisorSum % j == 0:
                divisorSum2 += j
    if divisorSum2 == i:
        amicableSum += i

print(amicableSum)