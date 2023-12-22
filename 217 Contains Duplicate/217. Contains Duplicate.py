def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        duplicatesList = []
        
        for I,N in enumerate(nums):
            if N not in duplicatesList and nums.index(N) == I:
                duplicatesList.append(N)    
            elif N in duplicatesList:
                duplicatesList.pop(duplicatesList.index(N))
        
        return True if not duplicatesList else False
        

print(\
    containsDuplicate([1,1,1,3,3,4,3,2,4,2]), # True
    containsDuplicate([1,2,3,4]) # False
)