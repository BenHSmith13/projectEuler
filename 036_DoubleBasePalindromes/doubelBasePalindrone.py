__author__ = 'bensmith'

answer = 0

for i in range(1000000):
        pal = str(i)
        for j in range(len(pal)//2):
            if pal[j] != pal[(len(pal)-1) - j]:
                break
        else:
            print(i, end=" ")
            pal = str(bin(i))
            for j in range(2, len(pal)//2+1):
                if pal[j] != pal[len(pal) - j + 1]:
                    print()
                    break
            else:
                print(bin(i))
                answer += i

print(answer)