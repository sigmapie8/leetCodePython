'''
Kadane's Algo
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -99999999999
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if(curr_sum > max_sum):
                max_sum = curr_sum
            if(curr_sum < 0):
                curr_sum = 0
 
        return max_sum
