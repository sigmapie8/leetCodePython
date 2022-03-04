class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for index, num in enumerate(nums):
            remaining = target - num;       
            try:
                if(num_map[remaining] is not None):
                    return [num_map[remaining], index]
            except:
                num_map[num] = index
