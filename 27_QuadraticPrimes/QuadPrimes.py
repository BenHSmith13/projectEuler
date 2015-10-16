__author__ = 'bensmith'


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in xrange(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def longest_quad_prime():
    longest = []
    prod = 0
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            temp = []
            n = 0
            while is_prime(n*n + a*n + b):
                temp.append(n*n + a*n + b)
                n += 1
            if len(temp) > len(longest):
                longest = temp
                prod = a*b
    return prod


print (longest_quad_prime())
