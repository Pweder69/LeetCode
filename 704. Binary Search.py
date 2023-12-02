import math
def search( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    min  = 0 
    max = len(nums) 
    currA = nums[max//2]
    

    
    for x in range(int(round(math.log(max,2)))+1):
        # print(f"S  min: {min} max: {max} currI: {min+((max-min)//2)} currActual: {currA} currDIff: {max - min}")
        
        currIndex = min+((max-min)//2)
        currA = nums[currIndex]
        
        if currA < target:
            min = currIndex 
        if currA > target:
            max = currIndex 
        
        if currA == target:
            return currIndex
        
        print(f"E  min: {min} max: {max} currI: {currA} currActual: {currA} currDIff: {max - min}")
    return -1 

testnums = [9,15,17,24,27,29,36,42,47,49,51,53,54,55,71,77,78,86,88,91,92,98,100]

print(search(testnums,29))
# print(search([-1,0,3,5,9,12],2))