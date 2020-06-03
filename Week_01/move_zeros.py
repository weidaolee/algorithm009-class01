class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ori = 0
        for i in range(len(nums)):
            x = nums[i]
            if x != 0:
                nums[ori], nums[i] = nums[i], nums[ori]
                ori += 1
                print(nums)


z = Solution()
z.moveZeroes([5, 2, 0, 4, 0, 0, 1, 5, 3, 0, 0, 0, 1, 0])
