def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        duplicatesList = {}
        
        for I,N in enumerate(nums):
            if N not in duplicatesList and nums.index(N) == I:
                duplicatesList.append(N)    
            elif N in duplicatesList:
                return True
        return False
        
        

print(\
    containsDuplicate([1,1,2,3,4]), # True
    containsDuplicate([1,2,3,4]) # False
)