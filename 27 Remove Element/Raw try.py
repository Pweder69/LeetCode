class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        while True:
            try:
                nums.remove(val)
            except ValueError:
                return len(nums)


if __name__ == "__main__":
    sl = Solution()
    vals = [3,2,2,3]
    target = 3
    print(sl.removeElement(vals,target))
