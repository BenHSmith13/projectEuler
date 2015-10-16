__author__ = 'bensmith'

factorial = 1

for i in range(2, 101):
    factorial *= i

digits = str(factorial)
sum = 0
i = 0

while i < len(digits):
    sum += int(digits[i])
    i += 1

print(sum)