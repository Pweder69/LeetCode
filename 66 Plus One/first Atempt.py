class Solution:

    def recursiveEval(self, index, digits):
        value = digits[index]

        if value + 1 == 10:
            digits[index] = 0
            if index == 0 or index == -1 * len(digits):
                digits.insert(0, 0)
            self.recursiveEval(index - 1, digits)
        else:
            digits[index] += 1

    def plusOne(self, digits: list[int]) -> list[int]:

        if digits[-1] + 1 != 10:
            digits[-1] += 1
            return digits

        self.recursiveEval(-1, digits)
        return digits


if __name__ == "__main__":
    sl = Solution()
    values = [8, 9, 9, 9]

    print(sl.plusOne(values))
