class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        while(low <= high):
            mid = (low+high)//2
            if(isBadVersion(mid-1)):
                high = mid-1
                if(high < low):
                    high = low
            elif(isBadVersion(mid)):
                return mid
            else:
                low = mid+1
                if(low > high):
                    low = high
