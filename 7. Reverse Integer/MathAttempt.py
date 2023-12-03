import math


class Solution:
    def reverse(self, x: int) -> int:
        newInt = 0
        multiplier =1
        secondMultiplier  = len(str(x)) -1
        
        
        while True:
           addedValue = (x%(10** multiplier)) 
           if addedValue >=10:
               addedValue = addedValue//10
           
           
           multiplier +=1 
           x -= addedValue
           
           newInt += addedValue * (10 ** secondMultiplier)
           secondMultiplier -=1
           
           if x <= 0:
            return newInt  
        
    
    
sl = Solution()
print(sl.reverse(123))