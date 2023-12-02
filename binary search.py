
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def findNum(num,l):
    max = len(l) +1
    min = 0
    curIndex = int(min+((max-min)/2))
    
    while l[curIndex] != num:
        curIndex = int(min+((max-min)/2))
        
        if l[curIndex] < num:
            min = curIndex-1
            print(f"min:{min} max:{max} curr:{curIndex} currVal:{l[curIndex]} left")

        if l[curIndex] > num:
            max = curIndex+1
            print(f"min:{min} max:{max} curr:{curIndex} currVal:{l[curIndex]} right")

    return curIndex
    
print(findNum(29,primes))