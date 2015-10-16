__author__ = 'bensmith'


def make_permu_list():
    lst = []
    for i in range(10):                                         # digit 0
        perm = str(i)
        for j in range(10):                                     # digit 1
            if str(j) not in perm:
                permj = perm + str(j)
                for k in range(10):                                 # digit 2
                    if str(k) not in permj:
                        permk = permj + str(k)
                        for l in range(10):                             # digit 3
                            if str(l) not in permk:
                                perml = permk + str(l)
                                for m in range(10):                         # digit 4
                                    if str(m) not in perml:
                                        permm = perml + str(m)
                                        for n in range(10):                     # digit 5
                                            if str(n) not in permm:
                                                permn = permm + str(n)
                                                for o in range(10):                 # digit 6
                                                    if str(o) not in permn:
                                                        permo = permn + str(o)
                                                        for p in range(10):             # digit 7
                                                            if str(p) not in permo:
                                                                permp = permo + str(p)
                                                                for q in range(10):         # digit 8
                                                                    if str(q) not in permp:
                                                                        permq = permp + str(q)
                                                                        for r in range(10):     # digit 9
                                                                            if str(r) not in permq:
                                                                                permr = permq + str(r)
                                                                                lst.append(permr)
    return lst


print (make_permu_list()[1000000 - 1])
