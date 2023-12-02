
def twoSum(numbers, target):

    
    
    for index in range(len(numbers)//2):
        
        # print(numbers[index],numbers[(index*-1)-1])
        
        currentPoint= numbers[index]
        inversePoint = numbers[(index*-1)-1]
        
        if  (currentPoint + inversePoint) == target:
            return currentPoint, inversePoint
    return False

print(twoSum([2,7,11,15],9))         
