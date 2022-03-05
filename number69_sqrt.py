class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        Binary search
        '''
        low = 0
        high = (x//3)+1
        mid = (high+low)//2
        while(mid >= low and mid <= high):
            if(mid*mid > x):
                high = mid-1
            elif(mid*mid < x):
                low = mid+1
            else:
                return mid
            mid = (high+low)//2
        
        return mid
