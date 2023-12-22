import math


def Palindromes(x):
    xList = []
    for char in str(x):
        xList.append(char)

    IndexAmount = len(xList) - 1
    halfIndexAmount = range(1, int(math.floor(IndexAmount) / 2) + 1)

    for index in halfIndexAmount:
        reverseVal = xList[len(xList) - index]
        originalVal = xList[index - 1]

        if originalVal != reverseVal:
            return False
    return True


print(Palindromes(10))
