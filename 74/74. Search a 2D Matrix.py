import time

def searchMatrix( matrix: list[list[int]], target: int) -> bool:
    
    matrixRows = len(matrix) 
    matrixColls = len(matrix[0]) 
    
    min =0
    max = matrixRows * matrixColls
    
    lastMin = min
    lastMax = max
    
    while True:
        curIndex = (min + (max-min)//2)
        print(f"{(curIndex//2)}  {curIndex%3} {curIndex}")
        # print(f"V:{curVal} I:{curIndex} ma{max} mi:{min} "  )
       
        
        curVal = matrix[curIndex//matrixColls][curIndex% matrixColls]
        
        
        if curVal < target: # adjusts max and min to cross out the non possibilities. 
            min = curIndex
        elif curVal > target:
            max = curIndex
        
        if curVal == target:
            return True
        
        if (lastMin == min) and (lastMax == max): #debounce the loop as if the max and min stay the same we know that 
            return False                          # It hasent found it and its at its last loop.
        lastMin = min
        lastMax = max
        

m = [[0,1,2],[3,4,5]]
print(searchMatrix(m,5))
