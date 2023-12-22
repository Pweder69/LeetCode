import math


def Palindromes(x):
    if str(x) == str(x)[::-1]: return True
    return False


print(Palindromes(1221))
