class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 1 
        
        for n in range(1, len(nums)):
            print(nums)
            if nums[n] != nums[n - 1]:
                nums[i] = nums[n]
                i += 1

        return i