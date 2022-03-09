class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:        
        distinct = set(nums)
        return len(distinct) != len(nums)
