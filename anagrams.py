def isAnagram(s: str, t: str) -> bool:
    l = list(s)

    for c in t:
        if len(t) != len(s) or c not in l:
            return False
        elif c in l:
            l.pop(l.index(c))
            print(f"poped {c} list{l}")

    return True


print(isAnagram("aa", "acc"))
