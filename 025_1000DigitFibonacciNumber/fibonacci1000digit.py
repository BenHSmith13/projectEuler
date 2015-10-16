__author__ = 'bensmith'

x = 1
y = 1
ct = 2
fibStr = str(x)
digits = len(fibStr)

while digits < 1000:
    temp = y
    y = x
    x += temp
    ct += 1
    fibStr = str(x)
    digits = len(fibStr)

print(ct)