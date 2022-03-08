class Solution:
    def addDigits(self, num: int) -> int:
        if(num <= 0):
            return num
        else:
            m = num%9
            if(m == 0): return 9
            return m
