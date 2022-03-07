class Solution:
    
    def __init__(self):
        self.t = {}
    
    def climbStairs(self, n: int) -> int:
        '''
        It is basically an A.P.
        '''
        if(n == 1):
            return 1
        elif(n == 2):
            return 2
        else:
            try:
                return self.t[n-1]+self.t[n-2]
            except:
                self.t[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
                return self.t[n]
