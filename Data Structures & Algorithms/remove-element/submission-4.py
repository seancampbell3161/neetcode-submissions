class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_list = nums[:]
        
        print(nums)

        for num in new_list:
            if num == val:
                print('hit')
                nums.remove(num)
        return len(nums)