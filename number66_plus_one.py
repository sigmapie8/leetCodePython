class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int("".join([str(x) for x in digits]))
        return [x for x in str(number+1)]
