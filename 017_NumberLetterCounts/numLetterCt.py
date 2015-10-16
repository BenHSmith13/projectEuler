__author__ = 'bensmith'

word = ""

for i in range(1, 1001):
    #word = ""
    toString = str(i)
    lastDigit = int(toString[len(toString) - 1])
    secondToLast = 0
    if i > 99:
        if 99 < i < 200:
            word += "OneHundred"
        if 199 < i < 300:
            word += "TwoHundred"
        if 299 < i < 400:
            word += "ThreeHundred"
        if 399 < i < 500:
            word += "FourHundred"
        if 499 < i < 600:
            word += "FiveHundred"
        if 599 < i < 700:
            word += "SixHundred"
        if 699 < i < 800:
            word += "SevenHundred"
        if 799 < i < 900:
            word += "EightHundred"
        if 899 < i < 1000:
            word += "NineHundred"
        if i == 1000:
            word += "OneThousand"
        if i % 100 != 0:
            word += "And"
    if i > 9:
        secondToLast = int(toString[len(toString) - 2])
        if secondToLast == 1:
            if lastDigit == 0:
                word += "Ten"
            if lastDigit == 1:
                word += "Eleven"
            if lastDigit == 2:
                word += "Twelve"
            if lastDigit == 3:
                word += "Thirteen"
            if lastDigit == 4:
                word += "Fourteen"
            if lastDigit == 5:
                word += "Fifteen"
            if lastDigit == 6:
                word += "Sixteen"
            if lastDigit == 7:
                word += "Seventeen"
            if lastDigit == 8:
                word += "Eighteen"
            if lastDigit == 9:
                word += "Nineteen"
        if secondToLast == 2:
            word += "Twenty"
        if secondToLast == 3:
            word += "Thirty"
        if secondToLast == 4:
            word += "Forty"
        if secondToLast == 5:
            word += "Fifty"
        if secondToLast == 6:
            word += "Sixty"
        if secondToLast == 7:
            word += "Seventy"
        if secondToLast == 8:
            word += "Eighty"
        if secondToLast == 9:
            word += "Ninety"
    if secondToLast != 1:
        if lastDigit == 1:
            word += "One"
        if lastDigit == 2:
            word += "Two"
        if lastDigit == 3:
            word += "Three"
        if lastDigit == 4:
            word += "Four"
        if lastDigit == 5:
            word += "Five"
        if lastDigit == 6:
            word += "Six"
        if lastDigit == 7:
            word += "Seven"
        if lastDigit == 8:
            word += "Eight"
        if lastDigit == 9:
            word += "Nine"
    #print(word)

print(len(word))