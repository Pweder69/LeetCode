def romanToInt(s: str) -> int:
    letterHash = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    lastLetter = 1
    total = 0
    for l in list(s[::-1]):

        currLetter = letterHash[l]

        if currLetter >= lastLetter:
            total += currLetter

        else:
            total -= currLetter
        lastLetter = currLetter

    return total


print(romanToInt("MCMXCIV"))

print(romanToInt("IV"))
