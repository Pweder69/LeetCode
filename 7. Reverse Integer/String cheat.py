import math

class Solution:
    def reverse(self, x: int) -> int:
        strVs = float(str(x)[::-1])
        return strVs if math.log2(strVs) <= 32  else 0
    


if __name__ == "__main__":
    SL = Solution()
    
    print(SL.reverse(123))