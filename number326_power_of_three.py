class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while(int(n) >= 3):
            n = n/3      
        return n==1
