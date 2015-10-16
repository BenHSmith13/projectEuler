__author__ = 'bensmith'

numerator = 11
denominator = 11

#ex 49/98 = 4/8

for i in range(11, 99):
    for j in range(11, 99):
        if i != j:
            iStr = str(i)
            jStr = str(j)
            for k in iStr