__author__ = 'bensmith'

answer = 0

for i in range(2, 999999):
    digitSum = 0
    toString = str(i)
    for j in toString:
        toNum = ord(j) - 48
        digitSum += toNum**5
    if digitSum == i:
        answer += i

print(answer)