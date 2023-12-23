from typing import List
import unittest


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1:
            return strs[0]

        currPrefix = ""  # dont need to prime loop because every string __contains__ ""

        for lOfFirstWord in range(1, len(strs[0]) + 1):
            currentPrefixSegment = strs[0][:lOfFirstWord]
            for words in strs:
                if currentPrefixSegment != words[:lOfFirstWord]:
                    return currPrefix

            currPrefix = strs[0][:lOfFirstWord]  # update the prefix after it passes through all words
        return currPrefix


class LongestCommonPrefixTest(unittest.TestCase):

    def test_1(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(["flower", "flow", "flight"]), "fl")

    def test_2(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(["dog", "racecar", "car"]), "")

    def test_3(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(["dog"]), "dog")

    def test_4(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(["", ""]), "")

    def test_5(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(["ab", "a"]), "a")

    def test_6(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(["flower", "flower", "flower", "flower"]), "flower")

    def test_7(self):
        solution = Solution()
        self.assertEqual(solution.longestCommonPrefix(["c", "acc", "ccc"]), "")


if __name__ == "__main__":
    unittest.main()
