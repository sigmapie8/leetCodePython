class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        result = []
        for num in nums:
            if(num):
                result.append(num)
            else:
                zero_count += 1
        
        nums[:] = result[:] + [0 for x in range(zero_count)]
