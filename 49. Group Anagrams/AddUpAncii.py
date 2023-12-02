
class Solution:
    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) <= 1: 
            # Redundancy for empty or singular strings
            return [strs]  
        
        final = [] 
        # Creates the return Value

        for i, currString in enumerate(strs):
            strGVal = sum(ord(l) for l in currString ) 
            # Gets the ANCII Value for the current group
            
            final.append(list(currString)) #creats the group 
            
            strs.pop(i) # Removes the first value that created the group

            for otherString in strs.copy():
                otherValue = sum(ord(l) for l in otherString) 
                # Creates the ANCII addup for every iteration in Str

                if otherValue == strGVal: # checks if the group value and iteration value are the same 
                    strs.remove(otherString) # if equal removes the value and adds it to the group
                    final[i].append(otherString)

        if strs != [] and strs is not None: #adds all singular groups groups with no other anagrams.
            final.append(strs)

        return final 
        

solution = Solution()

print(solution.groupAnagrams(["","",""]))