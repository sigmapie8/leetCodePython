class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        rotation = k%length
        nums[:] = nums[length-rotation:length]+nums[0:length-rotation]
