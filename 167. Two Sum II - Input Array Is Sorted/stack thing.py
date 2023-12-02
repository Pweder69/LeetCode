

def twoSum(numbers, target):
    ansList = {}
    
    for curIndex, currNum in enumerate(numbers):
        
        solutionToCurr = target - currNum
        
        if solutionToCurr in ansList:
            return [curIndex +1,ansList[solutionToCurr] +1][::-1]
        
        ansList[currNum] = curIndex
    
print(twoSum([-1,0],-1))
        