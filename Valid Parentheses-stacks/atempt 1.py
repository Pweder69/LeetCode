def isValid(s: str) -> bool:
    map = {")": "(", "}": "{", "]": "["}

    for index, char in enumerate(list(s)):
        for key, item in map.items():
            if str(char) == key and str(s[len(s) - index - 1]) == item and index < (len(list(s)) - 1) / 2:
                return True
            print(f"{char.encode()} {s[len(s) - index - 1]} ")

        return False


print(isValid("()"))
