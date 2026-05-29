class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        count = 0
        while count < 2:
            for n in nums:
                ans.append(n)
            count += 1

        return ans